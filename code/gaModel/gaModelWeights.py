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
import gaModel.GAModelP_AVR as gaModelP_AVR

import earthquake.catalog as catalog

bins = list()

def evaluationFunction(individual, year, catalogo, region):
	qntYears=5
	depth = 100

	definicao=models.model.loadModelDefinition('../params/'+region+'Etas_'+str(depth)+'.txt')
	for i in range(qntYears):
		observations=list()
		observacao=models.model.newModel(definicao, mag=False)
		observacao=models.model.addFromCatalog(observacao, catalogo, year)
		# observacao.bins = observacao.bins.tolist()
		observacao.values4poisson = list(individual)
		observations.append(observacao)
	modelo=gaModelP_AVR.gaModel(20,50,0.9,0.1,observations,year+qntYears,region, depth)
	modelo.values4poisson= list(individual)
	global bins
	bins = modelo.bins
	return modelo.loglikelihood[0],


	

toolbox = base.Toolbox()

creator.create("FitnessFunction", base.Fitness, weights=(1.0,))
creator.create("Individual", array.array, typecode='d', fitness=creator.FitnessFunction)
# Attribute generator
# TODO: mudar aqui pra receber os pesos ja
# talvez nao seja esse
toolbox.register("attr_float", random.random)


toolbox.register("mate", tools.cxOnePoint)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mutate", tools.mutPolynomialBounded,indpb=0.1, eta = 1, low = 0, up = 1)

#parallel
pool = multiprocessing.Pool()
toolbox.register("map", pool.map)

def gaModel(NGEN, n, CXPB,MUTPB, modelOmega,year,region, mean, depth=100):

	
	definicao=models.model.loadModelDefinition('../params/'+region+'Etas_'+str(depth)+'.txt')
	catalogo=catalog.readFromFile('../data/SC-catalog.dat')
	catalogo=catalog.filter(catalogo,definicao)
	toolbox.register("evaluate", evaluationFunction, year=year, catalogo=catalogo, region=region)
	# toolbox.register("individual", modelOmega[0].values4poisson)
	toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, len(modelOmega[0].values4poisson))
	toolbox.register("population", tools.initRepeat, list, toolbox.individual)
	
	pop = toolbox.population(n)

	for ind in pop:
		for i in range(len(ind)):
			ind[i] = modelOmega[0].values4poisson[i]

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

	generatedModel = type(modelOmega[0])
	generatedModel.loglikelihood = evaluationFunction(best_pop, year, catalogo, region)
	generatedModel.values4poisson = best_pop
	
	generatedModel.bins = bins
	return generatedModel


if __name__ == "__main__":
	gaModel()