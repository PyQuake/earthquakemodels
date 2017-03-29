#!/usr/bin/env python
import sys, math, random
sys.path.insert(0, '../code')
import models.model as model
import gaModel.gaModel_Yuri as ga
import numpy as np

qntYears = 5
year=2001
region ='EastJapan'

observations = list()
means = list()
logbook = list()
for i in range(qntYears):
    observation = model.loadModelDB(region+'jmaData', year+i)
    observation.bins = observation.bins.tolist()
    observations.append(observation)
    means.append(observation.bins)
del observation
mean = np.mean(means, axis=0)
    
# For black box function optimization, we can ignore the first 5 arguments. 
# The remaining arguments specify parameters using this format: -name value 

tournsize = 0 

for i in range(len(sys.argv)-1):  
    if (sys.argv[i] == '-tournsize'):
        tournsize = int(sys.argv[i+1])
 
# Compute the branin function:
loglikelihood = ga.gaModel(
        NGEN=100,
        CXPB=0.9,
        MUTPB=0.1,
        modelOmega=observations,
        year=year +
        qntYears,
        region=region,
        mean=mean,
        tournsize=tournsize,
        n_aval=50000)

  
# SMAC has a few different output fields; here, we only need the 4th output:
print ("Result of algorithm run: SUCCESS, 0, 0, %f, 0" % loglikelihood)
 

