#Need to fix the import section to use only need files

import time
from deap import base, creator, tools
import numpy
from csep.loglikelihood import calcLogLikelihood as loglikelihood
from models.mathUtil import calcNumberBins
#TODO: change this line to import only needed files
import models.model
import random
import array

def initDEAP():
    toolbox = base.Toolbox()
    toolbox.register("evaluate", evaluationFunction, modelOmega=modelOmega)
    creator.create("FitnessFunction", base.Fitness, weights=(1.0,))
    creator.create("Individual", array.array, typecode='d', fitness=creator.FitnessFunction)
    # Attribute generator
    toolbox.register("attr_float", random.random)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, len(modelOmega.bins))

    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("mate", tools.cxBlend, alpha = 0.5)
    toolbox.register("select", tools.selRoulette)
    toolbox.register("mutate", tools.mutPolynomialBounded,indpb=0.05, eta = 1, low = 0, up = 1)

    stats = tools.Statistics(key=lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)

    logbook = tools.Logbook()
    logbook.header = "gen","min","avg","max","std"

def evaluationFunction(individual, modelOmega):
    
    logValue = float('Infinity')
    modelLambda=type(modelOmega[0])
    
    for i in range(len(modelOmega)):
        modelLambda.bins=list(individual)
        modelLambda.bins=calcNumberBins(modelLambda.bins, modelOmega[i].bins)    
        tempValue=loglikelihood(modelLambda, modelOmega[i])

        if tempValue < logValue:
            logValue = tempValue

    return logValue,

def gaModel(NGEN,CXPB,MUTPB,modelOmega,year,n=500):

    #Should this go to initDEAP????
    toolbox = base.Toolbox()
    toolbox.register("evaluate", evaluationFunction, modelOmega=modelOmega)
    creator.create("FitnessFunction", base.Fitness, weights=(1.0,))
    creator.create("Individual", array.array, typecode='d', fitness=creator.FitnessFunction)
    # Attribute generator
    toolbox.register("attr_float", random.random)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, len(modelOmega[0].bins))

    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("mate", tools.cxBlend, alpha = 0.5)
    toolbox.register("select", tools.selRoulette)
    toolbox.register("mutate", tools.mutPolynomialBounded,indpb=0.05, eta = 1, low = 0, up = 1)

    stats = tools.Statistics(key=lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)

    logbook = tools.Logbook()
    # logbook.header = "gen","time","min","avg","max","std"
    starttime = time.time()

    pop = toolbox.population(n)
    # Evaluate the entire population

    fitnesses = list(map(toolbox.evaluate, pop))#need to pass 2 model.bins. One is the real data, the other de generated model
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    for g in range(NGEN):
        print("NGEN: ", g)
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
        for i in range(len(invalid_ind)):
            for j in range(len(invalid_ind[i])):
                if(invalid_ind[i][j] < 0):
                    invalid_ind[i][j] = -invalid_ind[i][j]
                if(invalid_ind[i][j] > 1):
                    invalid_ind[i][j] = random.random()

        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        # The population is entirely replaced by the offspring, but the last pop best_ind
        #Elitism
        best_ind = tools.selBest(pop, 1)[0]
        worst_ind = tools.selWorst(offspring, 1)[0]

        for i in range(len(offspring)):
            if offspring[i] == worst_ind:
                offspring[i] = best_ind
                break

        pop[:] = offspring  
        record = stats.compile(pop)
        logbook.record(gen=g,time=time.time()-starttime,**record)
    # f = open('../Zona/etasGaModel/gaModel'+str(year)+'_logbook.txt',"a")
    # f.write(str(logbook))
    # f.write('\n')

    best_ind = tools.selBest(pop, 1)[0]
    generatedModel = type(modelOmega[0])
    generatedModel.bins = list(best_ind)
    generatedModel.bins = calcNumberBins(generatedModel.bins, modelOmega[0].bins)
    generatedModel.definitions = modelOmega[0].definitions
    generatedModel.mag=False
    return generatedModel