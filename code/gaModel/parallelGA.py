#Need to fix the import section to use only need files
import sys
from deap import base, creator, tools
import numpy
from csep.loglikelihood import calcLogLikelihood as loglikelihood
from models.mathUtil import calcNumberBins
#TODO: change this line to import only needed files
import models.model
import random
import array
#Parallel
import multiprocessing
from mpi4py import MPI

import models.mathUtil as mathUtil
import earthquake.catalog as catalog
import models.model as model
import models.modelEtasGa as etasGa



def evaluationFunction(individual, modelOmega):
	"""
	This function calculates the loglikelihood of a model (individual) with 
	the real data from the prior X years (modelOmega, with length X).
	It selects the smallest loglikelihood value.
	"""
	logValue = float('Infinity')
	modelLambda=type(modelOmega[0])

	for i in range(len(modelOmega)):
		modelLambda.bins=list(individual)
		modelLambda.bins=calcNumberBins(modelLambda.bins, modelOmega[i].bins)
		tempValue=loglikelihood(modelLambda, modelOmega[i])

		if tempValue < logValue:
			logValue = tempValue

	return logValue,


def gaModel(NGEN, n, CXPB,MUTPB, modelOmega,year,region, mean, depth=100, FREQ = 10):
	"""
	The main function. It evolves models, namely modelLamba or individual. 
	This applies the gaModel with a circular island model
	It uses two parallel system: 1, simple, that splits the ga evolution between cores
	and 2, that distributes the islands
	"""
	

	creator.create("FitnessFunction2", base.Fitness, weights=(1.0,))

	toolbox = base.Toolbox()

	creator.create("Individual", array.array, typecode='d', fitness=creator.FitnessFunction2)
	# Attribute generator
	toolbox.register("attr_float", random.random)
	toolbox.register("evaluate", evaluationFunction, modelOmega=modelOmega)
	toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, len(modelOmega[0].bins))
	toolbox.register("population", tools.initRepeat, list, toolbox.individual)


	toolbox.register("mate", tools.cxOnePoint)
	# operator for selecting individuals for breeding the next
	# generation: each individual of the current generation
	# is replaced by the 'fittest' (best) of three individuals
	# drawn randomly from the current generation.
	toolbox.register("select", tools.selTournament, tournsize=3)
	toolbox.register("mutate", tools.mutPolynomialBounded,indpb=0.1, eta = 1, low = 0, up = 1)

	#multiprocessing parallel
	pool = multiprocessing.Pool()
	toolbox.register("map", pool.map)


	pop = toolbox.population(n)

	# logbook = tools.Logbook()
	# logbook.header = "min","avg","max","std"
	stats = tools.Statistics(key=lambda ind: ind.fitness.values)
	stats.register("avg", numpy.mean)
	stats.register("std", numpy.std)
	stats.register("min", numpy.min)
	stats.register("max", numpy.max)

	# Evaluate the entire population
	fitnesses = list(map(toolbox.evaluate, pop))#need to pass 2 model.bins. One is the real data, the other de generated model
	for ind, fit in zip(pop, fitnesses):
		ind.fitness.values = fit

	#1 to NGEN
	#creating comm and island model not fixed
	target = 0
	info = MPI.Status()
	comm = MPI.COMM_WORLD
	size = comm.Get_size()
	rank = comm.Get_rank()
	origin = (rank - (target+1)) % size
	dest = (rank + ((target+1) + size)) % size

	mpi_info = MPI.Info.Create()

	# logbook = tools.Logbook()
	# logbook.header = "rank","gen", "depth","min","avg","max","std"
	# stats = tools.Statistics(key=lambda ind: ind.fitness.values)
	# stats.register("avg", numpy.mean)
	# stats.register("std", numpy.std)
	# stats.register("min", numpy.min)
	# stats.register("max", numpy.max)

	for g in range(NGEN):
		# Select the next generation individuals
		#nao tem
		offspring = toolbox.select(pop, len(pop))
		# Clone the selected individuals{}
		# offspring = [toolbox.clone(ind) for ind in population]
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

    
		fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
		for ind, fit in zip(invalid_ind, fitnesses):
			ind.fitness.values = fit

        # The population is entirely replaced by the offspring, but the last island[rank] best_pop
        #Elitism
		best_pop = tools.selBest(pop, 1)[0]
		worst_ind = tools.selWorst(offspring, 1)[0]
		for i in range(len(offspring)):
			if offspring[i] == worst_ind:
				offspring[i] = best_pop
				break

		pop[:] = offspring

		#migrastion
			
		if g % (FREQ-1) == 0 and g > 0:
			best_inds = tools.selBest(pop, 1)[0]
			data = comm.sendrecv(sendobj=best_inds,dest=dest,source=origin)
			#rotation
			target+=1
			origin = (rank - (target+1)) % size
			dest = (rank + ((target+1) + size)) % size

			pop[random.randint(0, len(pop)-1)] = ind
			del best_pop
			del data
			
		#logBook
		record = stats.compile(pop)
		logbook.record(gen=g,  depth=depth,**record)
	print(logbook)

	# choose the best value
	if rank == 0:
		best_pop=tools.selBest(pop, 1)[0]
		lista = list()
		lista.append(best_pop)
		for thread in range(size):
			if (thread != 0):
				req = comm.irecv(source=thread)
				data = req.wait()
				lista.append(data)
		maximo =  float('-inf')
		for value, index in zip(lista, range(len(lista))):
			maximo_local = evaluationFunction(value, modelOmega)
			if maximo < maximo_local[0]:
				theBestIndex = index
				maximo = maximo_local[0]
				best_pop = value
	else: 
		best_pop=tools.selBest(pop, 1)[0]
		comm.send(best_pop, dest=0)

	generatedModel = type(modelOmega[0])
	generatedModel.prob = best_pop
	generatedModel.bins = calcNumberBins(best_pop, modelOmega[0].bins)
	generatedModel.loglikelihood = best_pop.fitness.values
	generatedModel.definitions = modelOmega[0].definitions
	generatedModel.mag=True


	return generatedModel

if __name__ == "__main__":
	gaModel()