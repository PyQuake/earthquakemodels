"""
This GA code uses a simplified version of the gaModel where only some bins are considered.
"""
from numba import jit
from operator import attrgetter
from deap import base, creator, tools
import numpy
from csep.loglikelihood import calcLogLikelihood 
from models.mathUtil import calcNumberBins
import models.model
import random
import array
from pathos.multiprocessing import ProcessingPool as Pool
import time 
from functools import lru_cache as cache

@jit
def evaluationFunction(individual, modelOmega, mean):
	"""
	This function calculates the loglikelihood of a model (individual) with 
	the real data from the prior X years (modelOmega, with length X).
	It selects the smallest loglikelihood value.
	"""
	logValue = float('Inf')
	genomeModel=models.model.convertFromListToData(individual,len(modelOmega[0].bins))
	modelLambda=models.model.newModel(modelOmega[0].definitions)
	modelLambda.bins=calcNumberBins(genomeModel.bins, mean)
	for i in range(len(modelOmega)):    
		tempValue=calcLogLikelihood(modelLambda, modelOmega[i])
		calcLogLikelihood.cache_clear()
		if tempValue < logValue:
			logValue = tempValue
	return logValue,


def mutationFunction(individual, indpb, length):
	"""
	This function changes a ind (individual) by selecting new values given a probabilistic value (indpb).
	The new values are random values. It may change a ind more than once
	It uses the length of the ind to cover all of its bins.
	"""
	for i in range(length):
		if random.random()<indpb:
			individual[i].index=random.randint(0 ,length-1)
		if random.random()<indpb:
			individual[i].prob=random.random()
	return individual

#parallel

toolbox = base.Toolbox()
creator.create("FitnessFunction", base.Fitness, weights=(1.0,))
creator.create("Individual", numpy.ndarray, fitness=creator.FitnessFunction)
pool = Pool()
toolbox.register("map", pool.map)

def gaModel(NGEN,CXPB,MUTPB,modelOmega,year,region, mean, n_aval=50000):
	"""
	The main function. It evolves models, namely modelLamba or individual. 
	This version of the GA simplifies the ga using a list of bins with occurences
	It uses 1 parallel system: 1, simple, that splits the ga evolution between cores
	"""
	#defining the class (list) that will compose an individual
	class genotype():
	    def __init__(self):
	    	self.index = random.randint(0, len(modelOmega[0].bins)-1)
	    	self.prob = random.random()
	
	y=int(n_aval/NGEN)
	x=n_aval - y*NGEN
	n= x + y

	# Calculate the len of the gen
	lengthPos=dict()
	tempValue=0
	for i in range(len(modelOmega)):    
		for j in range(len(modelOmega[i].bins)):
			if modelOmega[i].bins[j] != 0:
				lengthPos[str(j)] = 1
	length=len(lengthPos)


	toolbox = base.Toolbox()
	creator.create("FitnessFunction", base.Fitness, weights=(1.0,))
	toolbox.register("evaluate", evaluationFunction, modelOmega=modelOmega, mean= mean)
	toolbox.register("individual", tools.initRepeat, creator.Individual, genotype, n=length)
	toolbox.register("population", tools.initRepeat, list, toolbox.individual)
	toolbox.register("mate", tools.cxOnePoint)
	# operator for selecting individuals for breeding the next
	# generation: each individual of the current generation
	# is replaced by the 'fittest' (best) of three individuals
	# drawn randomly from the current generation.
	# toolbox.register("select", tools.selTournament, tournsize=tournsize)
	toolbox.register("select", tools.selRoulette)
	toolbox.register("mutate", mutationFunction,indpb=0.1, length=length)

	stats = tools.Statistics(key=lambda ind: ind.fitness.values)
	stats.register("avg", numpy.mean)
	stats.register("std", numpy.std)
	stats.register("min", numpy.min)
	stats.register("max", numpy.max)

	logbook = tools.Logbook()
	logbook.header = "gen","min","avg","max","std"

	pop = toolbox.population(n)

	fitnesses = list(map(toolbox.evaluate, pop))#need to pass 2 model.bins. One is the real data, the other de generated model

	for ind, fit in zip(pop, fitnesses):
		ind.fitness.values = fit
	# exit()

	for g in range(NGEN):
		# normalize fitnesses
		tempFitness=[]
		tempFitness[:] = fitnesses
		min = numpy.min(fitnesses)
		max = numpy.max(fitnesses)
		fitnesses[:] = (fitnesses-min)/(max-min)
		# Select the next generation individuals
		offspring = toolbox.select(pop, len(pop))
		#de-normalize
		fitnesses=tempFitness
		#create offspring
		offspring = list(map(toolbox.clone, pop))
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
			
        # The population is entirely replaced by the offspring, but the last ind replaced by best_pop
        #Elitism
		best_pop = tools.selBest(pop, 1)[0]
		offspring = sorted(offspring, key=attrgetter("fitness"), reverse = True)
		offspring[len(offspring)-1]=best_pop
		random.shuffle(offspring)

		pop[:] = offspring
		#logBook
		record = stats.compile(pop)
		logbook.record(gen=g, **record)
	
	
	generatedModel=models.model.newModel(modelOmega[0].definitions)
	generatedModel.bins = [0.0]*len(modelOmega[0].bins)
	generatedModel = models.model.convertFromListToData(best_pop,len(modelOmega[0].bins))
	generatedModel.prob = generatedModel.bins
	# generatedModel.bins = calcNumberBins(generatedModel.bins, modelOmega[0].bins)
	generatedModel.bins=calcNumberBins(generatedModel.bins, mean)
	generatedModel.definitions = modelOmega[0].definitions
	generatedModel.loglikelihood = best_pop.fitness.values
	generatedModel.logbook = logbook

	# output = generatedModel.loglikelihood 
	# return((-1)*output[0])


	
	return generatedModel

if __name__ == "__main__":
	gaModel()