#Need to fix the import section to use only need files
from deap import base, creator, tools
import numpy
from csep.loglikelihood import calcLogLikelihood as loglikelihood
from models.mathUtil import calcNumberBins
#TODO: change this line to import only needed files
import models.model
import random
import array



def equalObjects(x,y):
    return x.prob==y.prob and x.index==y.index
        
def evaluationFunction(individual, modelOmega):

    logValue = float('Infinity')
    modelLambda=type(modelOmega[0])
    modelLambda=models.model.convertFromListToData(individual,len(modelOmega[0].bins))    

    for i in range(len(modelOmega)):    
        tempValue=loglikelihood(modelLambda, modelOmega[i])

        if tempValue < logValue:
            logValue = tempValue

    return logValue,


def mutationFunction(individual, indpb, definitions, length):
 
    for i in range(length):
        if random.random()<indpb:
            individual[i].index=random.randint(0 ,length-1)
            individual[i].prob=random.random()
    return individual


def gaModel(type_m, NGEN,CXPB,MUTPB,modelOmega,year, region, depth, n_aval=50000):
	global length
	length=0

	class genotype():
	    def __init__(self):
	    	self.index = random.randint(0, len(modelOmega[0].bins)-1)
	    	self.prob = random.random()
	y=int(n_aval/NGEN)
	x=n_aval - y*NGEN
	n= x + y

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
	toolbox.register("select", tools.selTournament, tournsize=3)
	toolbox.register("mutate", mutationFunction,indpb=0.1, definitions=modelOmega[0].definitions, length=len(modelOmega[0].bins)-1)

	stats = tools.Statistics(key=lambda ind: ind.fitness.values)
	stats.register("avg", numpy.mean)
	stats.register("std", numpy.std)
	stats.register("min", numpy.min)
	stats.register("max", numpy.max)

	logbook = tools.Logbook()
	logbook.header = "gen", "depth","min","avg","max","std"

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
		record = stats.compile(pop)

		logbook.record(ngen=g, depth=depth, **record)

	print(logbook)
	if (type_m == 'clustered'):
		f = open('../Zona2/logbook_listaGA_newClustered/'+region+'_'+str(year)+'_'+depth+'_logbook.txt',"a")
	else:
		f = open('../Zona2/logbook_listaGA_new/'+region+'_'+str(year)+'_'+depth+'_logbook.txt',"a")
	f.write(str(logbook))
	f.write('\n')
	f.close()
	
	generatedModel = type(modelOmega[0])
	generatedModel.bins = [0.0]*len(modelOmega[0].bins)
	generatedModel = models.model.convertFromListToData(best_pop,len(modelOmega[0].bins))
	generatedModel.prob = generatedModel.bins
	generatedModel.bins = calcNumberBins(generatedModel.bins, modelOmega[0].bins)
	generatedModel.definitions = modelOmega[0].definitions
	generatedModel.mag=True
	generatedModel.loglikelihood = best_pop.fitness.values

	#for pysmac
	# logValue = best_pop.fitness.values
	#return logValue
	
	
	# gen = logbook.select("ngen")
	# fit_max=logbook.select("max")
	# fit_std = logbook.select("std")
	# print(gen, fit_std, fit_max)


	# import matplotlib.pyplot as plt

	# fig, ax1 = plt.subplots()

	# line1 = ax1.plot(gen, fit_max, "b-", label="Maximum Fitness")
	# ax1.set_xlabel("Generation")
	# ax1.set_ylabel("Fitness", color="b")
	# for tl in ax1.get_yticklabels():
	   # tl.set_color("b")

	# ax2 = ax1.twinx()
	# line2 = ax2.plot(gen, fit_std, "r-", label="STD fitness")
	# ax2.set_ylabel("STD", color="r")
	# for tl in ax2.get_yticklabels():
	#      tl.set_color("r")

	# lns = line1
	# labs = [l.get_label() for l in lns]
	# ax1.legend(lns, labs, loc="center right")

	# plt.savefig('../Zona2/logbook_listaGA_new/'+region+'_'+str(year)+'_convergencia_media.png')
	return generatedModel
