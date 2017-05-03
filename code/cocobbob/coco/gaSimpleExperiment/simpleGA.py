"""
This GA code creates the gaModel 
"""
import sys
sys.path.insert(0, '../../../')
from deap import base, creator, tools
import numpy
from csep.loglikelihood import calcLogLikelihood
from models.mathUtil import calcNumberBins
import models.model
import random
import array
from operator import attrgetter
# from pathos.multiprocessing import ProcessingPool as Pool
# from multiprocessing import Pool


def evalFun(individual, fun):
	return fun(individual),
#parallel
toolbox = base.Toolbox()
creator.create("FitnessFunction", base.Fitness, weights=(-1.0,))
creator.create("Individual", array.array, typecode='d', fitness=creator.FitnessFunction)

def gaModel(fun, problem_dimension, NGEN=100,CXPB=0.9,MUTPB=0.1, n_aval=50000):
	"""
	The main function. It evolves models, namely modelLamba or individual. 
	It uses 1 parallel system: 1, simple, that splits the ga evolution between cores
	""" 
	# Attribute generator
	toolbox.register("attr_float", random.uniform, 0,5)
	toolbox.register("mate", tools.cxOnePoint)
	# operator for selecting individuals for breeding the next
	# generation: each individual of the current generation
	# is replaced by the 'fittest' (best) of three individuals
	# drawn randomly from the current generation.
	toolbox.register("select", tools.selLexicase)
	# toolbox.register("select", tools.selLexicase)
	toolbox.register("mutate", tools.mutPolynomialBounded,indpb=0.1, eta = 1, low = -5, up = 5)

	stats = tools.Statistics(key=lambda ind: ind.fitness.values)
	stats.register("avg", numpy.mean)
	stats.register("std", numpy.std)
	stats.register("min", numpy.min)
	stats.register("max", numpy.max)

	#calculating the number of individuals of the populations based on the number of executions
	y=int(n_aval/NGEN)
	x=n_aval - y*NGEN
	n= x + y

	toolbox.register("evaluate", evalFun, fun=fun)
	#TODO: Adjust
	toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, problem_dimension)
	toolbox.register("population", tools.initRepeat, list, toolbox.individual)

	logbook = tools.Logbook()
	logbook.header = "gen","min","avg","max","std"

	pop = toolbox.population(n)
	# Evaluate the entire population
	fitnesses = list(toolbox.map(toolbox.evaluate, pop))#need to pass 2 model.bins. One is the real data, the other de generated model
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
        #The population is entirely replaced by the offspring, but the last ind replaced by best_pop
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

	return best_pop

if __name__ == "__main__":
	gaModel()
