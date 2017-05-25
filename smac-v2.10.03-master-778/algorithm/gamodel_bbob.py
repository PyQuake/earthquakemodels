#!/usr/bin/python
import sys
from deap import base, creator, tools
import numpy as np
# from csep.loglikelihood import calcLogLikelihood
# from models.mathUtil import calcNumberBins
# import models.model
import random
import array
from operator import attrgetter
# from scoop import futures
# import fgeneric
# import bbobbenchmarks as bn


toolbox = base.Toolbox()
creator.create("FitnessFunction", base.Fitness, weights=(-1.0,))
creator.create(
    "Individual",
    array.array,
    typecode='d',
    fitness=creator.FitnessFunction
)
# pool = Pool()
# toolbox.register("map", futures.map)


def tupleize(func):
    """A decorator that tuple-ize the result of a function. This is useful
    when the evaluation function returns a single value.
    """
    def wrapper(*args, **kargs):
        return func(*args, **kargs),
    return wrapper


def gaModel(func,
            NGEN,
            CXPB,
            MUTPB,
            modelOmega,
            year,
            region,
            mean,
            n_aval,
            tournsize,
            ftarget
            ):
    """The main function. It evolves models, namely modelLamba or individual.
    """

    # start = time.clock()
    # Attribute generator
    toolbox.register("attr_float", random.random)
    toolbox.register("mate", tools.cxOnePoint)
    toolbox.register("select", tools.selTournament, tournsize=2)
    toolbox.register(
        "mutate",
        tools.mutPolynomialBounded,
        indpb=0.1,
        eta=1,
        low=0,
        up=1
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

    toolbox.register("evaluate", func, modelOmega=modelOmega, mean=mean)
    toolbox.decorate("evaluate", tupleize)
    toolbox.register(
        "individual",
        tools.initRepeat,
        creator.Individual,
        toolbox.attr_float,
        len(modelOmega[0].bins)
    )
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    # logbook = tools.Logbook()
    # logbook.header = "gen","min","avg","max","std"

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
                toolbox.mate(child1, child2)
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
        offspring = sorted(offspring, key=attrgetter("fitness"), reverse=True)
        offspring[0] = best_pop
        random.shuffle(offspring)
        pop[:] = offspring
        record = stats.compile(pop)
        # logbook.record(gen=g, **record)
        if (abs(record["min"] - ftarget)) < 10e-8:
            return best_pop
        if record["std"] < 10e-12:
            sortedPop = sorted(pop, key=attrgetter("fitness"), reverse=True)
            pop = toolbox.population(n)
            pop[0] = sortedPop[0]
            pop = toolbox.population(n)
            fitnesses = list(toolbox.map(toolbox.evaluate, pop))
            for ind, fit in zip(pop, fitnesses):
                ind.fitness.values = fit
            g += 1
            record = stats.compile(pop)
            # logbook.record(gen=g, **record)

    return best_pop


if __name__ == "__main__":
    for i in range(len(sys.argv) - 1):
        print(sys.argv[i])
        if (sys.argv[i] == '-tournsize'):
            tournsize = int(sys.argv[i + 1])
        elif (sys.argv[i] == '-region'):
            region = sys.argv[3]
    print(region, tournsize)
    # return 2
    # exit()
    # f = open(gaParams, "r")
    # keys = ['key', 'NGEN', 'n_aval', 'qntYears', 'CXPB', 'MUTPB']

    # params = dict()
    # for line in f:
    #     if line[0] == '#':
    #         continue
    #     tokens = line.split()
    #     for key, value in zip(keys, tokens):
    #         if key == 'key':
    #             params[key] = value
    #         elif key == 'CXPB' or key == 'MUTPB':
    #             params[key] = float(value)
    #         elif key == 'region':
    #             params[key] = value
    #         else:
    #             params[key] = int(value)
    # f.close()
    # # Create a COCO experiment that will log the results under the
    # # ./output directory
    # e = fgeneric.LoggingFunction(output)

    # observations = list()
    # means = list()
    # for i in range(params['qntYears']):
    #     observation = models.model.loadModelDB(region + 'jmaData', year + i)
    #     observation.bins = observation.bins.tolist()
    #     observations.append(observation)
    #     means.append(observation.bins)
    # # del observation
    # mean = np.mean(means, axis=0)
    # param = (params['region'], params['year'], params['qntYears'])
    # func, opt = bn.instantiate(2, iinstance=1, param=param)
    # observation = models.model.loadModelDB(
    #     region + 'jmaData', year + params['qntYears'] + 1)
    # ftarget = calcLogLikelihood(observation, observation)
    # del observation
    # e.setfun(func, opt=ftarget)

    # gaModel(e.evalfun,
    #         NGEN=params['NGEN'],
    #         CXPB=params['CXPB'],
    #         MUTPB=params['MUTPB'],
    #         modelOmega=observations,
    #         year=params['year'] +
    #         params['qntYears'],
    #         region=params['region'],
    #         mean=mean,
    #         n_aval=params['n_aval'],
    #         tournsize=params['tournsize'],
    #         ftarget=e.ftarget)
    # # print('ftarget=%.e4 FEs=%d fbest-ftarget=%.4e and
    # # fbest = %.4e' % (e.ftarget, e.evaluations, e.fbest - e.ftarget, e.fbest))
    # # e.finalizerun()
    # # return e.fbest
    # # print('date and time: %s' % time.asctime())
