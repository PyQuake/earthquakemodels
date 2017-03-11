#!/usr/bin/env python3
import sys
sys.path.insert(0, '..')
import models.model as model
import gaModel.parallelGA as parallelGA
import gaModel.parallelReducedModel as parallelReducedModel
import numpy as np
#from mpi4py import MPI

def execParallelGA(year, region, qntYears=5, times=10):
    """
    Creates the GAModel with SC catalog with parallel and distributed island model
    """
    observations = list()
    means = list()
    for i in range(qntYears):
        observation = model.loadModelDB(region+'jmaData', year+i)
        observation.bins = observation.bins.tolist()
        observations.append(observation)
        means.append(observation.bins)
    mean = np.mean(means, axis=0)
    for i in range(times):
        model_=model.model()
        model_ = parallelGA.gaModel(
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
        model_.modelName = region+'parallelGA' 
        parallelGA_ = model.loadModelDB(region+'parallelGA', year)
        # if (parallelGA_.definitions==None):    
        #     model.saveModelDB(model_)


def callParallelGA(region):
    """
    It is a wrapper to the function that generates the parallel GAModel
    It cover the years of 2000 to 2005, and the models are from 2005 to 2010
    """
    year = 2000
    while(year <= 2005):
        execParallelGA(year, region)
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
    callParallelGA(region)

    

    region = 'EastJapan'
    year = 2000
    callParallelGA(region)


    region = 'Tohoku'
    year = 2000
    callParallelGA(region)

        
    region = 'Kansai'
    year = 2000
    callParallelGA(region)


if __name__ == "__main__":
    main()
