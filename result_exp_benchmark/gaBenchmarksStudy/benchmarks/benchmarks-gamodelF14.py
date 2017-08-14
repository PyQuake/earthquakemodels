#!/usr/bin/python
#    This file is part of DEAP.
#
#    DEAP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    DEAP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with DEAP. If not, see <http://www.gnu.org/licenses/>.
import sys
# sys.path.insert(0, '../../../')
import array
import random
from deap import base
from deap import creator
from deap import tools
import fgeneric
import numpy as np
from operator import attrgetter

import bbobbenchmarks as bn

toolbox = base.Toolbox()
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", array.array, typecode="d",
               fitness=creator.FitnessMin)
# pool = multiprocessing.Pool()
# toolbox.register("map", futures.map)


def tupleize(func):
    """A decorator that tuple-ize the result of a function. This is useful
    when the evaluation function returns a single value.
    """
    def wrapper(*args, **kargs):
        return func(*args, **kargs),
    return wrapper


def main(func,
         NGEN,
         CXPB,
         MUTPB,
         dim,
         ftarget,
         tournsize,
         n_aval
         ):
    toolbox.register("attr_float", random.random)
    toolbox.register("select", tools.selTournament, tournsize=tournsize)
    toolbox.register(
        "mutate",
        tools.mutGaussian,
        mu=0,
        sigma=1,
        indpb=0.1
    )
    stats = tools.Statistics(key=lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)
    # calculating the number of individuals of the
    # populations based on the number of executions
    y = int(n_aval / NGEN)
    x = n_aval - y * NGEN
    n = x + y

    toolbox.register("evaluate", func)
    toolbox.decorate("evaluate", tupleize)
    toolbox.register("attr_float", random.uniform, -4, 4)
    toolbox.register("mate", tools.cxUniform)
    toolbox.register("individual", tools.initRepeat, creator.Individual,
                     toolbox.attr_float, dim)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    logbook = tools.Logbook()
    logbook.header = "gen", "min", "avg", "max", "std"
    pop = toolbox.population(n)
    # Evaluate the entire population
    # 2 model.bins: real data, generated model
    fitnesses = list(toolbox.map(toolbox.evaluate, pop))
    # numero_avaliacoes = len(pop)
    # normalize fitnesses
    # fitnesses = normalizeFitness(fitnesses)
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    for g in range(NGEN):
        # Select the next generation individuals
        offspring = toolbox.select(pop, len(pop))
        # create offspring
        offspring = list(toolbox.map(toolbox.clone, pop))
        # Apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2, 0.1)
                del child1.fitness.values
                del child2.fitness.values
        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values
        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = list(toolbox.map(toolbox.evaluate, invalid_ind))
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        # The population is entirely replaced by the offspring,
        # but the last ind replaced by best_pop
        # Elitism
        best_pop = tools.selBest(pop, 1)[0]
        offspring = sorted(offspring, key=attrgetter("fitness"))
        offspring[0] = best_pop
        random.shuffle(offspring)
        pop[:] = offspring
        record = stats.compile(pop)
        logbook.record(gen=g, **record)
        print(logbook.stream)
        if (record["min"] - ftarget) < 10e-8:
            return best_pop
        if record["std"] < 10e-12:
            best_pop = tools.selBest(pop, 1)[0]
            pop = toolbox.population(n)
            pop = sorted(pop, key=attrgetter("fitness"))
            pop[0] = best_pop
            fitnesses = list(toolbox.map(toolbox.evaluate, pop))
            for ind, fit in zip(pop, fitnesses):
                ind.fitness.values = fit
            g += 1
            record = stats.compile(pop)
            logbook.record(gen=g, **record)
            print(logbook.stream)
    return best_pop


if __name__ == "__main__":
    for i in range(len(sys.argv) - 1):
        if (sys.argv[i] == '-tournsize'):
            tournsize = int(sys.argv[i + 1])
        elif (sys.argv[i] == '-year'):
            year = int(sys.argv[i + 1])
        elif (sys.argv[i] == '-params'):
            gaParams = sys.argv[i + 1]
        elif (sys.argv[i] == '-region'):
            region = sys.argv[i + 1]

    f = open(gaParams, "r")
    keys = ['key', 'NGEN', 'n_aval', 'qntYears', 'CXPB', 'MUTPB']

    params = dict()
    for line in f:
        if line[0] == '#':
            continue
        tokens = line.split()
        for key, value in zip(keys, tokens):
            if key == 'key':
                params[key] = value
            elif key == 'CXPB' or key == 'MUTPB':
                params[key] = float(value)
            else:
                params[key] = int(value)
    f.close()
    # Maximum number of restart for an algorithm that detects stagnation

    # Create a COCO experiment that will log the results under the
    # ./output directory
    e = fgeneric.LoggingFunction('output')

    # Iterate over all desired test dimensions
    # for dim in (2, 3, 5, 10, 20, 40):
    dim = 10
    # Set the maximum number function evaluation granted to the algorithm
    # This is usually function of the dimensionality of the problem

    # Iterate over a set of benchmarks (noise free benchmarks here)
    # for f_name in bn.nfreeIDs:
    f_name = 14
    # Iterate over all the instance of a single problem
    # Rotation, translation, etc.
    # for instance in chain(range(1, 6), range(21, 31)):
    instance = 1
    # Set the function to be used (problem) in the logger
    e.setfun(*bn.instantiate(f_name, iinstance=1))

    # Independent restarts until maxfunevals or ftarget is reached
    # Run the algorithm with the remaining
    # number of evaluations
    main(e.evalfun,
         NGEN=params['NGEN'],
         CXPB=params['CXPB'],
         MUTPB=params['MUTPB'],
         dim=dim,
         n_aval=params['n_aval'],
         tournsize=tournsize,
         ftarget=e.ftarget)

    # Stop if ftarget is reached
    e.finalizerun()

    # print('f%d in %d-D, instance %d: FEs=%d with %d restarts, '
    #       'fbest-ftarget=%.4e, and best=%.4e'
    #       % (f_name, dim, instance, e.evaluations, restarts,
    #          e.fbest - e.ftarget, e.fbest))
    # print('date and time: %s' % time.asctime())
    print(e.ftarget)
