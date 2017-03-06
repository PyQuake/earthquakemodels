"""
This GA code creates the gaModel with a circular island model

"""
from operator import attrgetter
# import sys
from deap import base, creator, tools
import numpy
from csep.loglikelihood import calcLogLikelihood as loglikelihood
from models.mathUtil import calcNumberBins
import models.model
import random
import array
import multiprocessing
from mpi4py import MPI
import time 

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

#parallel
toolbox = base.Toolbox()
creator.create("FitnessFunction", base.Fitness, weights=(1.0,))
creator.create("Individual", array.array, typecode='d', fitness=creator.FitnessFunction)
pool = multiprocessing.Pool()
toolbox.register("map", pool.map)

def gaModel(NGEN,CXPB,MUTPB,modelOmega,year,region, mean, FREQ = 10, n_aval=50000):
	"""
	The main function. It evolves models, namely modelLamba or individual. 
	This applies the gaModel with a circular island model
	It uses two parallel system: 1, simple, that splits the ga evolution between cores
	and 2, that distributes the islands
	"""
	start = time.clock()  
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

	#calculating the number of individuals of the populations based on the number of executions
	y=int(n_aval/NGEN)
	x=n_aval - y*NGEN
	n= x + y

	pop = toolbox.population(n)

	logbook = tools.Logbook()
	logbook.header = "min","avg","max","std"
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

	logbook = tools.Logbook()
	logbook.header = "rank","gen","min","avg","max","std"
	stats = tools.Statistics(key=lambda ind: ind.fitness.values)
	stats.register("avg", numpy.mean)
	stats.register("std", numpy.std)
	stats.register("min", numpy.min)
	stats.register("max", numpy.max)

	for g in range(NGEN):
		# Select the next generation individuals
		offspring = toolbox.select(pop, len(pop))
		# Clone the selected individuals{}
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

        # The population is entirely replaced by the offspring, but the last island[rank] best_pop
        #Elitism
		best_pop = tools.selBest(pop, 1)[0]
		offspring = sorted(offspring, key=attrgetter("fitness"), reverse = True)
		offspring[len(offspring)-1]=best_pop

		pop[:] = offspring

		#migration
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
		logbook.record(gen=g, **record)

	# choose the best value
	if rank == 0:
		best_pop=tools.selBest(pop, 1)[0]
		best_all_pop = list()
		best_all_pop.append(best_pop)
		for thread in range(size):
			if (thread != 0):
				# local_best = comm.recv(source=thread)

				local_best = comm.recv(source=thread)
				# req = comm.irecv(source=thread)
				# local_best = req.wait()
				best_all_pop.append(local_best)
		maximum =  float('-inf')
		# for value, index in zip(best_all_pop, range(len(best_all_pop))):
		for local_best in best_all_pop:
			local_maximum = evaluationFunction(local_best, modelOmega)
			if maximum < local_maximum[0]:
				# theBestIndex = index
				maximum = local_maximum[0]
				best_pop = local_best
	else: 
		best_pop=tools.selBest(pop, 1)[0]
		comm.send(best_pop, dest=0)

	exit()
	end = time.clock()  
	generatedModel = type(modelOmega[0])
	generatedModel.prob = best_pop
	generatedModel.bins = calcNumberBins(best_pop, modelOmega[0].bins)
	generatedModel.loglikelihood = best_pop.fitness.values
	generatedModel.definitions = modelOmega[0].definitions
	generatedModel.time = start - end
	generatedModel.logbook = logbook

	return generatedModel

if __name__ == "__main__":
	gaModel()