#!/usr/bin/env python
import sys
sys.path.insert(0, '..')
import models.model as model
import gaModel.gaModel_Yuri as ga
import gaModel.reducedModel_Yuri as reducedGA
import numpy as np


def execReducedGAModel(year, region, qntYears=5, times=10):
    """
    Creates the list Model with JMA catalog
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
        model_ = reducedGA.gaModel(
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
        model_.modelName = region+'ReducedGAModel' 
        reducedGA_ = model.loadModelDB(region+'ReducedGAModel', year)
        # if (reducedGA_.definitions==None):    
        #     model.saveModelDB(model_)


def callReducedGAModel(region):
    """
    It is a wrapper to the function that generates the list model with JMA data
    It cover the years of 2000 to 2005, and the models are from 2005 to 2010
    """
    year = 2000
    while(year <= 2005):
        execReducedGAModel(year, region)
        year+=1

def main():
    """
    This function creates the needed enviroment needed to generate both GAModel and List Model with JMA catalog
    for the regions: EastJapan, Kanto, Kansai, Tohoku
    from 2000 to 2005 to create models from 2005 to 2010
    """
    region = 'Kanto'
    callReducedGAModel(region)

    region = 'EastJapan'
    year = 2000
    callReducedGAModel(region)

    region = 'Tohoku'
    year = 2000
    callReducedGAModel(region)

    region = 'Kansai'
    year = 2000
    callReducedGAModel(region)


if __name__ == "__main__":
    main()
