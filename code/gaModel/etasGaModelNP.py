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

global length
length=0

class genotype():
    def __init__(self):
        self.index=random.randint(0 ,length)
        self.prob=random.random()

def equalObjects(x,y):
    return x.prob==y.prob and x.index==y.index
        
def evaluationFunction(individual, modelOmega):

    logValue = float('Infinity')
    lambdasBins=list()

    for i in range(len(modelOmega)):        
        modelLambda=type(modelOmega[0])
        bins=models.model.convertFromListToData(individual,len(modelOmega[i].bins))    
        lambdasBins.append(bins)

    for i in range(len(modelOmega)):    
        
        modelLambda=models.model.convertFromListToData(individual,len(modelOmega[i].bins))    
        modelLambda.bins=lambdasBins[i].bins
        tempValue=loglikelihood(modelLambda, modelOmega[i])

        if tempValue < logValue:
            logValue = tempValue

    return logValue,

#enteder essa mutação...
def mutationFunction(individual, indpb, definitions, length):
    # i=0
    # while i<length:
    for i in range(length):
        if random.random()<indpb:
            individual[i].index=random.randint(0 ,length)
        # if random.random()<indpb:
            individual[i].prob=random.random()
    return individual


def gaModel(NGEN,CXPB,MUTPB,modelOmega, year, n=500):

    toolbox = base.Toolbox()
    toolbox.register("evaluate", evaluationFunction, modelOmega=modelOmega)
    creator.create("FitnessFunction", base.Fitness, weights=(1.0,))
    #TODO: Check if its posible to use it as obj, maybe, OFF
    creator.create("Individual", numpy.ndarray, fitness=creator.FitnessFunction)
    # numpy.ndarray((10,)
    # Attribute generator

    # Calculate the len of the gen by the mean of the Omegas size
    lengthList=list()
    tempValue=0
    for i in range(len(modelOmega)):    
        lengthList.append(len(modelOmega[i].bins)-1)
        tempValue+=lengthList[i]
    global length 
    length = int(tempValue/len(lengthList))

    toolbox.register("individual", tools.initRepeat, creator.Individual, genotype, n=length)

    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("mutate", mutationFunction,indpb=0.1, definitions=modelOmega[0].definitions, length=length)

    stats = tools.Statistics(key=lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)

    logbook = tools.Logbook()
    # logbook.header = "ngen","time","min","avg","max","std"
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
            # if offspring[i] == worst_ind:
            result = list(map(equalObjects,offspring[i],worst_ind))
            if all(result)==True:
                offspring[i] = best_ind
                print("Elitism")
                break

        pop[:] = offspring  
        record = stats.compile(pop)
        logbook.record(ngen=g,time=time.time()-starttime,**record)
    f = open('../Zona/etasGaModel/etasGaModelNP_'+str(year)+'_logbook.txt',"a")
    f.write(str(logbook))
    f.write('\n')



    best_ind = tools.selBest(pop, 1)[0]
    generatedModel = type(modelOmega[0])
    generatedModel.bins = [0.0]*len(modelOmega[0].bins)
    generatedModel = models.model.convertFromListToData(best_ind,len(modelOmega[0].bins))
    generatedModel.prob = generatedModel.bins
    generatedModel.bins = calcNumberBins(generatedModel.bins, modelOmega[0].bins)
    generatedModel.definitions = modelOmega[0].definitions
    generatedModel.mag=True


    return generatedModel
