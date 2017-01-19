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
import multiprocessing
from mpi4py import MPI

class genotype():
    def __init__(self):
    	self.index = random.randint(0, 2024)
    	self.prob = random.random()


def equalObjects(x,y):
	"""
	Compares if two inds are equal
	"""
    return x.prob==y.prob and x.index==y.index
        
def evaluationFunction(individual, modelOmega):
	"""
	This function calculates the loglikelihood of a model (individual) with 
	the real data from the prior X years (modelOmega, with length X).
	It selects the smallest loglikelihood value.
	"""

    logValue = float('Infinity')
    modelLambda=type(modelOmega[0])
    modelLambda=models.model.convertFromListToData(individual,len(modelOmega[0].bins))    

    for i in range(len(modelOmega)):    
        tempValue=loglikelihood(modelLambda, modelOmega[i])

        if tempValue < logValue:
            logValue = tempValue

    return logValue,


def mutationFunction(individual, indpb, definitions, length):
 	"""
 	This function changes a ind (individual) by selecting new values given a probabilistic value (indpb).
 	The new values are random values. It may change a ind more than once

 	It uses the length of the ind to cover all of its bins.
	"""
    for i in range(length):
        if random.random()<indpb:
            individual[i].index=random.randint(0 ,length-1)
            individual[i].prob=random.random()
    return individual


def gaModel(NGEN, n, CXPB,MUTPB, modelOmega,year,region, mean, depth=100, FREQ = 10):
	"""
	The main function. It evolves models, namely modelLamba or individual. 
	This version of the GA simplifies the ga using a list of bins with occurences
	It uses two parallel system: 1, simple, that splits the ga evolution between cores
	and 2, that distributes the islands
	"""
	

	target = 0
	info = MPI.Status()
	comm = MPI.COMM_WORLD
	size = comm.Get_size()
	rank = comm.Get_rank()
	origin = (rank - (target+1)) % size
	dest = (rank + ((target+1) + size)) % size

	mpi_info = MPI.Info.Create()

	global length
	length=0

	toolbox = base.Toolbox()
	toolbox.register("evaluate", evaluationFunction, modelOmega=modelOmega)
	creator.create("FitnessFunction", base.Fitness, weights=(1.0,))
	#TODO: Check if its posible to use it as obj, maybe, OFF
	creator.create("Individual", numpy.ndarray, fitness=creator.FitnessFunction)

	# Calculate the len of the gen
	lengthPos=dict()
	tempValue=0
	for i in range(len(modelOmega)):    
		for j in range(len(modelOmega[i].bins)):
			lengthPos[str(j)]=1

	length=len(lengthPos)

	toolbox.register("individual", tools.initRepeat, creator.Individual, genotype, n=length)
	toolbox.register("population", tools.initRepeat, list, toolbox.individual)
	toolbox.register("mate", tools.cxOnePoint)

	# operator for selecting individuals for breeding the next
	# generation: each individual of the current generation
	# is replaced by the 'fittest' (best) of three individuals
	# drawn randomly from the current generation.
	toolbox.register("select", tools.selTournament, tournsize=3)
	toolbox.register("mutate", mutationFunction,indpb=0.1, definitions=modelOmega[0].definitions, length=len(modelOmega[0].bins)-1)

	stats = tools.Statistics(key=lambda ind: ind.fitness.values)
	stats.register("avg", numpy.mean)
	stats.register("std", numpy.std)
	stats.register("min", numpy.min)
	stats.register("max", numpy.max)

	# logbook = tools.Logbook()
	# logbook.header = "gen", "depth","min","avg","max","std"

	#parallel loop	
	pool = multiprocessing.Pool()
	toolbox.register("map", pool.map)

	pop = toolbox.population(n)

	fitnesses = list(map(toolbox.evaluate, pop))#need to pass 2 model.bins. One is the real data, the other de generated model

	for ind, fit in zip(pop, fitnesses):
		ind.fitness.values = fit
	for g in range(NGEN):
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
		best_pop = tools.selBest(pop, 1)[0]
		worst_ind = tools.selWorst(offspring, 1)[0]
		
		for i in range(len(offspring)):
			result = list(map(equalObjects,offspring[i],worst_ind))
			if all(result)==True:
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
				data = comm.recv(source=thread)
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
	generatedModel.bins = [0.0]*len(modelOmega[0].bins)
	generatedModel = models.model.convertFromListToData(best_pop,len(modelOmega[0].bins))
	generatedModel.prob = generatedModel.bins
	generatedModel.bins = calcNumberBins(generatedModel.bins, modelOmega[0].bins)
	generatedModel.definitions = modelOmega[0].definitions
	generatedModel.mag=True
	generatedModel.loglikelihood = best_pop.fitness.values


	
	return generatedModel

if __name__ == "__main__":
	gaModel()