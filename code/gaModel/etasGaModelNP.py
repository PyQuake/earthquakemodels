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


def evaluationFunction(individual, modelOmega):
    modelLambda=type(modelOmega)
    modelLambda.bins=list(individual)
    modelLambda=models.model.convertFromListToData(individual,modelOmega)
    modelLambda.bins=calcNumberBins(modelLambda.bins, modelOmega.bins)
    logValue=loglikelihood(modelLambda, modelOmega)

    return logValue,

def mutationFunction(individual, indpb, definitions, length):
    i=0
    while i<length:
        if random.random()<indpb:
            individual[i]=random.randint(0 ,length)
        if random.random()<indpb:
            individual[i+1]=random.random()
        if random.random()<indpb:
            individual[i+2]=random.uniform(definitions[2]['min'], 
            definitions[2]['min'] + definitions[2]['cells']*definitions[2]['step'])
        i+=3
    return individual


def gaModel(NGEN,CXPB,MUTPB,modelOmega, year, n=500):

    toolbox = base.Toolbox()
    toolbox.register("evaluate", evaluationFunction, modelOmega=modelOmega)
    creator.create("FitnessFunction", base.Fitness, weights=(1.0,))
    #TODO: Check if its posible to use it as obj, maybe, OFF
    creator.create("Individual", array.array, typecode='d', fitness=creator.FitnessFunction)
    # Attribute generator
    #TODO: Em andamento... OFF
    lengthList=len(modelOmega.bins)-1
    # lengthList=numpy.count_nonzero(modelOmega.bins)
    # lengthList+=round(((-1)+random.uniform(0.0,2.0))*(n*0.1))
    toolbox.register("attr_index", random.randint,0 ,lengthList)

    toolbox.register("attr_mag", random.uniform, modelOmega.definitions[2]['min'], 
        modelOmega.definitions[2]['min'] + modelOmega.definitions[2]['cells']*modelOmega.definitions[2]['step'])

    toolbox.register("attr_prob", random.random)   

    toolbox.register("individual", tools.initCycle, creator.Individual,
                 (toolbox.attr_index, toolbox.attr_prob, toolbox.attr_mag), n=lengthList)

    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("mate", tools.cxOnePoint)
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("mutate", mutationFunction,indpb=0.1, definitions=modelOmega.definitions, length=lengthList)

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
    f = open('../Zona/etasGaModel/etasGaModelNP_'+str(year)+'_logbook.txt',"a")
    f.write(str(logbook))
    f.write('\n')



    best_ind = tools.selBest(pop, 1)[0]
    generatedModel = type(modelOmega)
    generatedModel.bins = [0.0]*len(modelOmega.bins)
    generatedModel = models.model.convertFromListToData(best_ind,modelOmega)
    generatedModel.bins = calcNumberBins(generatedModel.bins, modelOmega.bins)
    generatedModel.definitions = modelOmega.definitions
    generatedModel.mag=True
    #TODO: Check if this is ok
    # for i,mag in zip(range(len(generatedModel.bins)), generatedModel.magnitudeValues):
    #     if mag==0.0:
    #         generatedModel.bins[i]=0

    return generatedModel
