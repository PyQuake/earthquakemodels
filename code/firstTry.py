#Need to fix the import section to use only need files

from deap import base, creator, tools
import numpy
from csep.loglikelihood import calcLogLikelihood as loglikelihood
from models.mathUtil import calcNumberBins
#TODO: change this line to import only needed files
import models.model
import random
import array
#Parallel
from scoop import futures
from time import time
import scoop

import models.mathUtil as mathUtil
import earthquake.catalog as catalog
import models.model as model
import multiprocessing



observations=list()
qntYears=5
# times=1
year=2005
region= 'Kanto'
depth=100

for i in range(qntYears):
    observation=model.loadModelFromFile('../Zona3/sc/3.0'+region+'real'+str(depth)+"_"+str(year+i)+'.txt')
    observation.bins=observation.bins.tolist()
    observations.append(observation)



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

creator.create("FitnessFunction2", base.Fitness, weights=(1.0,))



toolbox = base.Toolbox()

# pool = multiprocessing.Pool()
# toolbox.register("map", pool.map)

creator.create("FitnessFunction2", base.Fitness, weights=(1.0,))
creator.create("Individual", array.array, typecode='d', fitness=creator.FitnessFunction2)
# Attribute generator
toolbox.register("attr_float", random.random)
toolbox.register("evaluate", evaluationFunction, modelOmega=observations)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, len(observations[0].bins))
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


toolbox.register("mate", tools.cxOnePoint)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mutate", tools.mutPolynomialBounded,indpb=0.1, eta = 1, low = 0, up = 1)


#scoop parallel
toolbox.register("map", futures.map)


def gaModel(pop, NGEN,CXPB,MUTPB,modelOmega,year,region, depth, rank):
	# Evaluate the entire population

	stats = tools.Statistics(key=lambda ind: ind.fitness.values)
	stats.register("avg", numpy.mean)
	stats.register("std", numpy.std)
	stats.register("min", numpy.min)
	stats.register("max", numpy.max)

	#aui tem list na frente
	fitnesses = list(map(toolbox.evaluate, pop))#need to pass 2 model.bins. One is the real data, the other de generated model
	for ind, fit in zip(pop, fitnesses):
		ind.fitness.values = fit

	#1 to NGEN
	toolbox.unregister("attr_float")
    toolbox.unregister("individual")
    toolbox.unregister("population")
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
		# fitnesses = map(toolbox.evaluate, invalid_ind)
		for ind, fit in zip(invalid_ind, fitnesses):
			ind.fitness.values = fit

        # The population is entirely replaced by the offspring, but the last pop best_pop
        #Elitism
		best_pop = tools.selBest(pop, 1)[0]
		worst_ind = tools.selWorst(offspring, 1)[0]
		for i in range(len(offspring)):
			if offspring[i] == worst_ind:
				offspring[i] = best_pop
				break

		pop[:] = offspring
		record = stats.compile(pop)
		print(record, "'gen': ",g, "'rank': ", rank, "'cx': ",CXPB, "'mut': ",MUTPB)

	return best_pop, pop

def migrator():

	from mpi4py import MPI

	comm = MPI.COMM_WORLD
	size = comm.Get_size()
	rank = comm.Get_rank()

	cx = random.random()
	mut = 1 - cx

	pop = toolbox.population(n=250)

	#send the pop + the best from the other thread, run for 10 gen then mingration
	#TODO: var the par cx an mut
	listMigrators = [None] * size
	for times in range(10):

		source = (rank - (times+1)) % size
		dest = (rank + ((times+1) + size)) % size

		toMigrate, pop = gaModel(pop, 10,cx,mut,observations,year+qntYears,region, depth, rank)
		listMigrators[rank]  = toMigrate

		req = comm.isend(listMigrators[rank], dest=dest)
		data = comm.recv(source=source)

		worst_ind = tools.selWorst(pop, 1)[0]
		for i in range(len(pop)):
			if pop[i] == worst_ind:
				pop[i] = data
				break

	best_local = tools.selBest(pop, 1)[0]

	theBestIndex = -1

	if rank == 0:
		lista = list()
		lista.append(best_local)
		for thread in range(size):
			if (thread != 0):
				lista.append(comm.recv(source=thread))
		maximo =  float('-inf')
		for value, index in zip(lista, range(len(lista))):
			maximo_local = evaluationFunction(value, observations)
			if maximo < maximo_local[0]:
				theBestIndex = index
				maximo = maximo_local[0]

		
	else: 
		comm.send(best_local, dest=0)
	


if __name__ == "__main__":
	migrator()
	

















