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
from scoop import futures
import fgeneric
import bbobbenchmarks as bn

toolbox = base.Toolbox()
creator.create("FitnessFunction", base.Fitness, weights=(-1.0,))
creator.create("Individual", array.array, typecode='d', fitness=creator.FitnessFunction)
# pool = Pool()
toolbox.register("map", futures.map)

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
	#calculating the number of individuals of the populations based on the number of executions
	y=int(n_aval/NGEN)
	x=n_aval - y*NGEN
	n= x + y
	# Attribute generator
	toolbox.register("evaluate", func, modelOmega = modelOmega, mean=mean)
	@tupleize
	def evaluate(func):
		return func()

	# toolbox.decorate("evaluate", tupleize)

	toolbox.register("attr_float", random.random)
	toolbox.register("mate", tools.cxTwoPoint)
	# operator for selecting individuals for breeding the next
	# generation: each individual of the current generation
	# is replaced by the 'fittest' (best) of three individuals
	# drawn randomly from the current generation.
	toolbox.register("select", tools.selTournament, tournsize=tournsize)
	# toolbox.register("select", tools.selLexicase)
	toolbox.register("mutate", tools.mutPolynomialBounded,indpb=0.1, eta = 1, low = 0, up = 1)
	stats = tools.Statistics(key=lambda ind: ind.fitness.values)
	stats.register("avg", np.mean)
	stats.register("std", np.std)
	stats.register("min", np.min)
	stats.register("max", np.max)
	# toolbox.register("evaluate", evaluationFunction, modelOmega=modelOmega, mean=mean)
	toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, len(modelOmega[0].bins))
	toolbox.register("population", tools.initRepeat, list, toolbox.individual)
	logbook = tools.Logbook()
	logbook.header = "gen","min","avg","max","std"

	pop = toolbox.population(n)
	# Evaluate the entire population
	fitnesses = list(toolbox.map(toolbox.evaluate, pop))
	for ind, fit in zip(pop, fitnesses):
		ind.fitness.values = fit

	for g in range(NGEN):
		print(g)
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
		#Elitism
		best_pop = tools.selBest(pop, 1)[0]
		# The population is entirely replaced by the offspring, but the last ind replaced by best_pop
		pop[:] = offspring

		fitnesses = list(toolbox.map(toolbox.evaluate, pop))
		for ind, fit in zip(pop, fitnesses):
			ind.fitness.values = fit
		pop = sorted(pop, key=attrgetter("fitness"), reverse = False)
		pop[0]=best_pop
		random.shuffle(pop)
		record = stats.compile(pop)
		logbook.record(gen=g,**record)
		if (abs(record["min"] - ftarget)) < 10e-8:
			print(logbook)
			return best_pop
		if record["std"] < 10e-12:	
			sortedPop = sorted(pop, key=attrgetter("fitness"), reverse = True)
			pop = toolbox.population(n)
			pop[0] = sortedPop[0]
			fitnesses = list(toolbox.map(toolbox.evaluate, pop))
			for ind, fit in zip(pop, fitnesses):
				ind.fitness.values = fit
			g+=1
	print(logbook)
	return best_pop

if __name__ == "__main__":
	output = sys.argv[1]
	tournsize = int(sys.argv[2])

	region = 'Kanto'
	year=2000

	# Create a COCO experiment that will log the results under the
	# ./output directory
	e = fgeneric.LoggingFunction(output)

	observations = list()
	means = list()
	for i in range(5):
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
		NGEN=10,
		CXPB=0.9,
		MUTPB=0.1,
		modelOmega=observations,
		year=year +
		5,
		region=region,
		mean=mean,
		n_aval=50,
		tournsize=tournsize,
		ftarget=e.ftarget)

	

	print(' FEs=%d fbest-ftarget=%.4e and fbest = %.4e'
	          % (e.evaluations, e.fbest - e.ftarget, e.fbest))
	e.finalizerun()
	print('date and time: %s' % time.asctime())