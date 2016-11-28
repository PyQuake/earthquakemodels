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
from time import time


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

	

toolbox = base.Toolbox()

creator.create("FitnessFunction", base.Fitness, weights=(1.0,))
creator.create("Individual", array.array, typecode='d', fitness=creator.FitnessFunction)
# Attribute generator
toolbox.register("attr_float", random.random)
toolbox.register("mate", tools.cxOnePoint)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mutate", tools.mutPolynomialBounded,indpb=0.1, eta = 1, low = 0, up = 1)

stats = tools.Statistics(key=lambda ind: ind.fitness.values)
stats.register("avg", numpy.mean)
stats.register("std", numpy.std)
stats.register("min", numpy.min)
stats.register("max", numpy.max)

#parallel
pool = multiprocessing.Pool()
toolbox.register("map", pool.map)

def gaModel(type_m, NGEN,CXPB,MUTPB,modelOmega,year,region, mean, depth=100, n_aval=50000):

	y=int(n_aval/NGEN)
	x=n_aval - y*NGEN
	n= x + y

	toolbox.register("evaluate", evaluationFunction, modelOmega=modelOmega)
	toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, len(modelOmega[0].bins))
	toolbox.register("population", tools.initRepeat, list, toolbox.individual)

	logbook = tools.Logbook()
	logbook.header = "gen", "depth","min","avg","max","std"

	pop = toolbox.population(n)
	# Evaluate the entire population

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
		for i in range(len(invalid_ind)):
			for j in range(len(invalid_ind[i])):
				if(invalid_ind[i][j] < 0):
					invalid_ind[i][j] = -invalid_ind[i][j]
				if(invalid_ind[i][j] > 1):
					invalid_ind[i][j] = random.random()

		fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
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
		
		#logBook
		record = stats.compile(pop)
		logbook.record(gen=g,  depth=depth,**record)
	# print(logbook)
	# if (type_m == 'clustered'):
	# 	f = open('../Zona2/logbook_gaModelClustered/'+region+'_'+str(year)+'_'+str(depth)+'_logbook.txt',"a")
	# elif (type_m == 'clusteredII'):
	# 	f = open('../Zona2/logbook_gaModelClusteredII/'+region+'_'+str(year)+'_'+str(depth)+'_logbook.txt',"a")
	# elif (type_m == 'non-clustered'):
	# 	f = open('../Zona2/logbook_gaModel/'+region+'_'+str(year)+'_'+str(depth)+'_logbook.txt',"a")
	# else:
	# 	f = open('../Zona2/synthetic/'+region+'_'+str(year)+'_'+str(depth)+'_logbook.txt',"a")
	# f.write(str(logbook))
	# f.write('\n')
	# f.close()
	
	generatedModel = type(modelOmega[0])
	generatedModel.prob = best_pop
	generatedModel.bins = calcNumberBins(best_pop, modelOmega[0].bins)
	generatedModel.loglikelihood = best_pop.fitness.values
	generatedModel.definitions = modelOmega[0].definitions
	generatedModel.mag=True
	#for pysmac
	# logValue = best_pop.fitness.values
	#return logValue

	# gen = logbook.select("gen")
	# fit_max=logbook.select("max")
	# fit_std = logbook.select("std")
	# print(gen, fit_std, fit_max)
	
	return generatedModel

if __name__ == "__main__":
	gaModel()