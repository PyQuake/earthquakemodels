"""
This GA code creates the gaModel 
"""
import sys
sys.path.insert(0, '../')
from deap import base, creator, tools
import numpy as np
from csep.loglikelihood import calcLogLikelihood
from models.mathUtil import calcNumberBins
import models.model
import random
import array
import time 
from operator import attrgetter
# from scoop import futures
import fgeneric
import bbobbenchmarks as bn
from functools import wraps


toolbox = base.Toolbox()
creator.create("FitnessFunction", base.Fitness, weights=(-1.0,))
creator.create("Individual", array.array, typecode='d', fitness=creator.FitnessFunction)
# pool = Pool()
# toolbox.register("map", futures.map)

def tupleize(func):
    """A decorator that tuple-ize the result of a function. This is useful
    when the evaluation function returns a single value.
    """
    def wrapper(*args, **kargs):
        return func(*args, **kargs),
    return wrapper

def gaModel(func,NGEN,CXPB,MUTPB,modelOmega,year,region, mean, n_aval, tournsize, ftarget):
	"""
	The main function. It evolves models, namely modelLamba or individual. 
	It uses 1 parallel system: 1, simple, that splits the ga evolution between cores
	"""
	start = time.clock()  
	# Attribute generator
	toolbox.register("attr_float", random.random)
	toolbox.register("mate", tools.cxOnePoint)
	# operator for selecting individuals for breeding the next
	# generation: each individual of the current generation
	# is replaced by the 'fittest' (best) of three individuals
	# drawn randomly from the current generation.
	toolbox.register("select", tools.selTournament, tournsize=2)
	# toolbox.register("select", tools.selLexicase)
	toolbox.register("mutate", tools.mutPolynomialBounded,indpb=0.1, eta = 1, low = 0, up = 1)

	stats = tools.Statistics(key=lambda ind: ind.fitness.values)
	stats.register("avg", numpy.mean)
	stats.register("std", numpy.std)
	stats.register("min", numpy.min)
	stats.register("max", numpy.max)

	#calculating the number of individuals of the populations based on the number of executions
	y=int(n_aval/NGEN)
	x=n_aval - y*NGEN
	n= x + y

	toolbox.register("evaluate", evaluationFunction, modelOmega=modelOmega, mean=mean)
	toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, len(modelOmega[0].bins))
	toolbox.register("population", tools.initRepeat, list, toolbox.individual)

	logbook = tools.Logbook()
	logbook.header = "gen","min","avg","max","std"

	pop = toolbox.population(n)
	# Evaluate the entire population
	fitnesses = list(toolbox.map(toolbox.evaluate, pop))#need to pass 2 model.bins. One is the real data, the other de generated model
	# normalize fitnesses
	# fitnesses = normalizeFitness(fitnesses)
	for ind, fit in zip(pop, fitnesses):
		ind.fitness.values = fit

	for g in range(NGEN):
		# Select the next generation individuals
		offspring = toolbox.select(pop, len(pop))
		#create offspring
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
        # The population is entirely replaced by the offspring, but the last ind replaced by best_pop
        #Elitism
		best_pop = tools.selBest(pop, 1)[0]
		offspring = sorted(offspring, key=attrgetter("fitness"), reverse = True)
		offspring[len(offspring)-1]=best_pop
		random.shuffle(offspring)
		pop[:] = offspring
		
		#logBook
		fitnesses = list(toolbox.map(toolbox.evaluate, pop))
		for ind, fit in zip(pop, fitnesses):
			ind.fitness.values = fit
		record = stats.compile(pop)
		logbook.record(gen=g, **record)
	print(logbook)
	return best_pop

if __name__ == "__main__":
	output = sys.argv[1]
	tournsize = int(sys.argv[2])
	region = sys.argv[3]
	year = int(sys.argv[4])
	gaParams = sys.argv[5]

	f = open(gaParams, "r")
	keys = ['key', 'geracao', 'aval', 'anos', 'cx', 'mut']
	params = dict()
	for line in f:
		if line[0] == '#':
			continue
		tokens = line.split()
		for key,value in zip(keys,tokens):
			print(key, value)
			if key == 'CXPB' or key == 'MUTPB':
				params[key] = float(value)
			else:
				params[key] = int(value)
	f.close()
	print(params)
	exit()

	# Create a COCO experiment that will log the results under the
	# ./output directory
	e = fgeneric.LoggingFunction(output)

	observations = list()
	means = list()
	for i in range(qntYears):
		observation = models.model.loadModelDB(region+'jmaData', year+i)
		observation.bins = observation.bins.tolist()
		observations.append(observation)
		means.append(observation.bins)
	del observation
	mean = np.mean(means, axis=0)
	param = (region, year)
	func, opt = bn.instantiate(2, iinstance=1, param=param)
	observation = models.model.loadModelDB(region+'jmaData', year+6)
	ftarget = calcLogLikelihood(observation, observation)
	e.setfun(func, opt=ftarget)

	gaModel(e.evalfun,
		NGEN=100,
		CXPB=0.9,
		MUTPB=0.1,
		modelOmega=observations,
		year=year +
		5,
		region=region,
		mean=mean,
		n_aval=50000,
		tournsize=tournsize,
		ftarget=e.ftarget)

	

	print('ftarget=%.e4 FEs=%d fbest-ftarget=%.4e and fbest = %.4e'
	          % (e.ftarget, e.evaluations, e.fbest - e.ftarget, e.fbest))
	e.finalizerun()
	print('date and time: %s' % time.asctime())