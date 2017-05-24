"""
This GA code creates the gaModel
"""
from numba import jit
from deap import base, creator, tools
import numpy
from csep.loglikelihood import calcLogLikelihood
from models.mathUtil import calcNumberBins
import models.model
import random
import array
import time
from operator import attrgetter
from pathos.multiprocessing import ProcessingPool as Pool
from functools import lru_cache as cache


@jit
def evaluationFunction(individual, modelOmega, mean):
    """
    This function calculates the loglikelihood of a model (individual) with
    the real data from the prior X years (modelOmega, with length X).
    It selects the smallest loglikelihood value.
    """
    logValue = float('Inf')
    genomeModel = models.model.newModel(modelOmega[0].definitions)
    genomeModel.bins = list(individual)
    modelLambda = models.model.newModel(modelOmega[0].definitions)
    modelLambda.bins = calcNumberBins(genomeModel.bins, mean)
    for i in range(len(modelOmega)):
        tempValue = calcLogLikelihood(modelLambda, modelOmega[i])
        calcLogLikelihood.cache_clear()
        if tempValue < logValue:
            logValue = tempValue
    return logValue,

# parallel


toolbox = base.Toolbox()
creator.create("FitnessFunction", base.Fitness, weights=(1.0,))
creator.create("Individual", array.array, typecode='d', fitness=creator.FitnessFunction)
pool = Pool()
toolbox.register("map", pool.map)


def gaModel(NGEN, CXPB, MUTPB, modelOmega, year, region, mean, tournsize=2, n_aval=50000):
    """
    The main function. It evolves models, namely modelLamba or individual.
    """
    start = time.clock()
    # Attribute generator
    toolbox.register("attr_float", random.random)
    toolbox.register("mate", tools.cxOnePoint)
    # operator for selecting individuals for breeding the next
    # generation: each individual of the current generation
    # is replaced by the 'fittest' (best) of three individuals
    # drawn randomly from the current generation.
    toolbox.register("select", tools.selTournament, tournsize=tournsize)
    toolbox.register("mutate", tools.mutPolynomialBounded, indpb=0.1, eta=1, low=0, up=1)

    stats = tools.Statistics(key=lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)

    # calculating the number of individuals of the populations based on the number of executions
    y = int(n_aval / NGEN)
    x = n_aval - y * NGEN
    n = x + y

    toolbox.register("evaluate", evaluationFunction, modelOmega=modelOmega, mean=mean)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, len(modelOmega[0].bins))
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    logbook = tools.Logbook()
    logbook.header = "gen", "min", "avg", "max", "std"

    pop = toolbox.population(n)
    # Evaluate the entire population
    # 2 model.bins: real data, generated model
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit
    for g in range(NGEN):
        if g % 10 == 0:
            print(g)
        # Select the next generation individuals
        offspring = toolbox.select(pop, len(pop))
        # Clone the selected individuals
        offspring = list(map(toolbox.clone, offspring))
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
        fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        # The population is entirely replaced by the offspring, but the last pop best_pop
        # Elitism
        best_pop = tools.selBest(pop, 1)[0]
        offspring = sorted(offspring, key=attrgetter("fitness"), reverse=True)
        offspring[len(offspring) - 1] = best_pop
        random.shuffle(offspring)
        pop[:] = offspring
        # logBook
        record = stats.compile(pop)
        logbook.record(gen=g, **record)
    end = time.clock()
    generatedModel = models.model.newModel(modelOmega[0].definitions)
    # conferir se e bins o best_pop
    generatedModel.prob = best_pop
    generatedModel.bins = calcNumberBins(list(best_pop), mean)
    generatedModel.loglikelihood = best_pop.fitness.values
    generatedModel.definitions = modelOmega[0].definitions
    generatedModel.time = start - end
    generatedModel.logbook = logbook
    # output = generatedModel.loglikelihood
    # return((-1)*output[0])
    print(logbook)
    exit()
    return generatedModel


if __name__ == "__main__":
    gaModel()
