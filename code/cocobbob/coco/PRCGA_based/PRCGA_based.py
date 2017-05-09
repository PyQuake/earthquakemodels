
#    This file is part of DEAP.
#
#    DEAP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    DEAP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with DEAP. If not, see <http://www.gnu.org/licenses/>.
import sys
sys.path.insert(0, '../../../')
sys.path.insert(0, '../code-postprocessing/aRTAplots/')
import array
import math
import random
import time

from itertools import chain

from deap import base
from deap import creator
from deap import benchmarks
from deap import tools
import fgeneric
import numpy
from operator import attrgetter

import bbobbenchmarks as bn

toolbox = base.Toolbox()
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", array.array, typecode="d", fitness=creator.FitnessMin)



def update(individual, mu, sigma):
    """Update the current *individual* with values from a gaussian centered on
    *mu* and standard deviation *sigma*.
    """
    for i, mu_i in enumerate(mu):
        individual[i] = random.gauss(mu_i, sigma)

def tupleize(func):
    """A decorator that tuple-ize the result of a function. This is useful
    when the evaluation function returns a single value.
    """
    def wrapper(*args, **kargs):
        return func(*args, **kargs),
    return wrapper

def main(func, dim, maxfuncevals, ftarget=None):
	NGEN=100
	CXPB=0.9
	MUTPB=0.1
	g=0
	n = min(100, 10 * problem_dimension)
	slicesize =int(n * 0.1)
	toolbox = base.Toolbox()
	toolbox.register("update", update)
	toolbox.register("evaluate", func)
	toolbox.decorate("evaluate", tupleize)
	toolbox.register("attr_float", random.uniform, -5,5)
	toolbox.register("mate", tools.cxTwoPoint)
	toolbox.register("select", tools.selTournament, tournsize=2)
	toolbox.register("mutate", tools.mutPolynomialBounded,indpb=0.1, eta = 1, low = -5, up = 5)
	stats = tools.Statistics(key=lambda ind: ind.fitness.values)
	stats.register("avg", numpy.mean)
	stats.register("std", numpy.std)
	stats.register("min", numpy.min)
	stats.register("max", numpy.max)
	toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, dim)
	toolbox.register("population", tools.initRepeat, list, toolbox.individual)
	logbook = tools.Logbook()
	logbook.header = "gen","min","avg","max","std"
	pop = toolbox.population(n)
	fitnesses = list(toolbox.map(toolbox.evaluate, pop))
	for ind, fit in zip(pop, fitnesses):
		ind.fitness.values = fit
	maxfuncevals -= len(pop)
	# for g in range(maxfuncevals):
	while(g < maxfuncevals):
		offspring = toolbox.select(pop, len(pop))
		offspring = list(toolbox.map(toolbox.clone, pop))
		for child1, child2 in zip(offspring[::2], offspring[1::2]):
			if random.random() < CXPB:
				toolbox.mate(child1, child2)
				del child1.fitness.values
				del child2.fitness.values
		for mutant in offspring:
			if random.random() < MUTPB:
				toolbox.mutate(mutant)
				del mutant.fitness.values
		best_pop = tools.selBest(pop, 1)[0]
		pop[:] = offspring

		fitnesses = list(toolbox.map(toolbox.evaluate, pop))
		for ind, fit in zip(pop, fitnesses):
			ind.fitness.values = fit
		pop = sorted(pop, key=attrgetter("fitness"), reverse = False)
		pop[0]=best_pop
		random.shuffle(pop)
		record = stats.compile(pop)
		if record["std"] < 1e-12:	
			sortedPop = sorted(pop, key=attrgetter("fitness"), reverse = True)
			pop = toolbox.population(n)
			pop[0:slicesize] = sortedPop[0:slicesize]
			fitnesses = list(toolbox.map(toolbox.evaluate, pop))
			for ind, fit in zip(pop, fitnesses):
				ind.fitness.values = fit
		logbook.record(gen=g, **record)
		g += len(pop)
	print(logbook)
	print(best_pop)
	# exit()
	#end my code

    
	# Create the desired optimal function value as a Fitness object
	# for later comparison
	opt = creator.FitnessMin((ftarget,))

	# Interval in which to initialize the optimizer
	interval = -5, 5
	sigma = (interval[1] - interval[0])/2.0
	alpha = 2.0**(1.0/dim)

	# Initialize best randomly and worst as a place holder
	best = creator.Individual(random.uniform(interval[0], interval[1]) for _ in range(dim))
	worst = creator.Individual([0.0] * dim)

	# Evaluate the first individual
	best.fitness.values = toolbox.evaluate(best)

	# Evolve until ftarget is reached or the number of evaluation
	# is exausted (maxfuncevals)
	for g in range(1, maxfuncevals):
		toolbox.update(worst, best, sigma)
		worst.fitness.values = toolbox.evaluate(worst)
		if best.fitness <= worst.fitness:
			# Incease mutation strength and swap the individual
			sigma = sigma * alpha
			best, worst = worst, best
		else:
			# Decrease mutation strength
			sigma = sigma * alpha**(-0.25)

	# Test if we reached the optimum of the function
	# Remember that ">" for fitness means better (not greater)
	if best.fitness > opt:
		print(best.fitness)
		exit()
		return best
	
	print(best.fitness)
	exit()
	return best

if __name__ == "__main__":
    # Maximum number of restart for an algorithm that detects stagnation
    maxrestarts = 1000
    
    # Create a COCO experiment that will log the results under the
    # ./output directory
    e = fgeneric.LoggingFunction("output")
    
    # Iterate over all desired test dimensions
    for dim in (10, 3, 5, 10, 20, 40):
        # Set the maximum number function evaluation granted to the algorithm
        # This is usually function of the dimensionality of the problem
        maxfuncevals = 100 * dim**2
        minfuncevals = dim + 2
        
        # Iterate over a set of benchmarks (noise free benchmarks here)
        for f_name in bn.nfreeIDs:
            
            # Iterate over all the instance of a single problem
            # Rotation, translation, etc.
            for instance in chain(range(1, 6), range(21, 31)):
                
                # Set the function to be used (problem) in the logger
                e.setfun(*bn.instantiate(f_name, iinstance=instance))
                
                # Independent restarts until maxfunevals or ftarget is reached
                for restarts in range(0, maxrestarts + 1):
                    if restarts > 0:
                        # Signal the experiment that the algorithm restarted
                        e.restart('independent restart')  # additional info
                    
                    # Run the algorithm with the remaining number of evaluations
                    revals = int(math.ceil(maxfuncevals - e.evaluations))
                    main(e.evalfun, dim, revals, e.ftarget)
                    
                    # Stop if ftarget is reached
                    if e.fbest < e.ftarget or e.evaluations + minfuncevals > maxfuncevals:
                        break
                
                e.finalizerun()
                
                print('f%d in %d-D, instance %d: FEs=%d with %d restarts, '
                      'fbest-ftarget=%.4e'
                      % (f_name, dim, instance, e.evaluations, restarts,
                         e.fbest - e.ftarget))
                         
            print('date and time: %s' % time.asctime())
