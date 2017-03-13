#!/usr/bin/env python3
import sys
sys.path.insert(0, '..')
import random
import earthquake.catalog as catalog
import models.model as model
import gaModel.GAModelP_AVR as gaModelP_AVR
import gaModel.parallelGAModelP_AVR as parallelGAModelP_AVR
import time
import numpy as np


def createRealModelSCwithP_AVR(
    year, region, qntYears=5, withMag=True, save=True):
    definicao = model.loadModelDefinition(
        '../params/'+region+'.txt')
    catalog_ = catalog.readFromFile('../data/SC-catalog.dat')
    catalog_ = catalog.filter(catalog_, definicao)
    observation = model.newModel(definicao)
    riskMap = catalog.readFromFileP_AVR(
        '../data/P_AVR-MAP_T30-TTL_TTL_TTL_TOTAL_I45_PS.csv')
    
    riskMap = catalog.filterP_AVR(riskMap, definicao)

    observation = model.addFromCatalogP_AVR(
        observation, catalog_, riskMap, year)

    if save == True:
        model.saveModelToFile(observation,
            '../Zona3/realSCwithP_AVR/' + region + 'real' + str(depth) + "_" + str(year) + '.txt', real=True)
 
def execParallelGA(year, region, qntYears=5, times=10):
    """
    Creates the GAModel with SC catalog with parallel and distributed island model
    """
    observations = list()
    means = list()
    for i in range(qntYears):
        observation = model.loadModelDB(region+'jmaData', year+i)
        aux = model.loadModelFromFile('../Zona3/realSCwithP_AVR/'
                                  + region + 'real' + str(depth) + "_" + str(year + i) + '.txt')    
        aux.values4poisson = [x+1 for x in aux.values4poisson]
        observation.values4poisson = aux.values4poisson
        del aux
        observation.bins = observation.bins.tolist()
        observations.append(observation)
        means.append(observation.bins)
    mean = np.mean(means, axis=0)
    for i in range(times):
        model_=model.model()
        model_ = parallelGAModelP_AVR.gaModel(
            NGEN=10,
            CXPB=0.9,
            MUTPB=0.1,
            modelOmega=observations,
            year=year +
            qntYears,
            region=region,
            mean=mean, 
            n_aval=50)
        model_.executionNumber=i
        model_.year=year+qntYears
        model_.modelName = region+'parallelGA' 
        parallelGA_ = model.loadModelDB(region+'parallelGA', year)
        # if (parallelGA_.definitions==None):    
        #     model.saveModelDB(model_)



def execGAModelwithP_AVR(year, region, depth, qntYears=5, times=10, save=True):

    observations = list()
    means = list()
    for i in range(qntYears):
        observation = model.loadModelDB(region+'jmaData', year+i)
        aux = model.loadModelFromFile('../Zona3/realSCwithP_AVR/'
                                  + region + 'real' + str(depth) + "_" + str(year + i) + '.txt')    
        observation.values4poisson = aux.values4poisson
        del aux
        observations.append(observation)
        means.append(observation.bins)
    mean = np.mean(means, axis=0)
    for i in range(times):
        model_ = gaModelP_AVR.gaModel(
            NGEN=100,
            CXPB=0.9,
            MUTPB=0.1,
            modelOmega=observations,
            year=year +
            qntYears,
            region=region,
            mean=mean)
        model_.executionNumber=i
        model_.year=year+qntYears
        model_.modelName = region+'GAModelwithP_AVR' 
        gaModelwithP_AVR_ = model.loadModelDB(region+'gaModelwithP_AVR_', year)
        # if (gaModelwithP_AVR.definitions==None):    
            # model.saveModelDB(model_)



def callGAModelwithP_AVR(region):
    """
    It is a wrapper to the function that generates the parallel  list model
    It cover the years of 2000 to 2005, and the models are from 2005 to 2010
    """
    year = 2000
    while(year <= 2005):
        execGAModelwithP_AVR(year, region)
        year+=1

def callParallelGAwithP_AVR(region):
    """
    It is a wrapper to the function that generates the parallel GAModel
    It cover the years of 2000 to 2005, and the models are from 2005 to 2010
    """
    year = 2000
    while(year <= 2005):
        execParallelGAwithP_AVR(year, region)
        year+=1



def main():
    """
    This function creates the needed enviroment needed to generate both, in parallel and distrituded,
     GAModel and List Model  with SC catalog
    for the regions: EastJapan, Kanto, Kansai, Tohoku
    from 2000 to 2005 to create models from 2005 to 2010
    """
    region = 'Kanto'
    year = 2000
    callGAModelwithP_AVR(region)
    callParallelReducedGAwithP_AVR(region)
    

    region = 'EastJapan'
    year = 2000
    callGAModelwithP_AVR(region)
    callParallelReducedGAwithP_AVR(region)
    
    region = 'Tohoku'
    year = 2000
    callGAModelwithP_AVR(region)
    callParallelReducedGAwithP_AVR(region)
            
    region = 'Kansai'
    year = 2000
    callGAModelwithP_AVR(region)
    callParallelReducedGAwithP_AVR(region)
    
if __name__ == "__main__":
    main()
