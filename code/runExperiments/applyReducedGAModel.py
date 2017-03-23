#!/usr/bin/env python
import sys
sys.path.insert(0, '..')
import models.model as model
import gaModel.reducedModel_Yuri as reducedGA
import numpy as np


def execReducedGAModel(year, region, qntYears=5, times=1):
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
        model_.modelName = region+'ReducedGAModel' 
        reducedGA_ = model.loadModelDB(region+'ReducedGAModel', year)
        print(model_.logbook)
        exit()
        # if (reducedGA_.definitions==None):    
        # #     model.saveModelDB(model_)
        #     model.saveModelToFile(model_,
        #         '../../Zona4/ReducedGAModel/' + region +'ReducedGAModel' + str(year+qntYears) + '_' + str(i) + '.txt')
        #     with open("../../Zona4/ReducedGAModel/" + region +"ReducedGAModel" + str(year+qntYears) + "_loglikelihood.txt", 'a') as f:
        #         f.write(str(model_.loglikelihood))
        #         f.write("\n")
        #         f.close()  

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

    # region = 'EastJapan'
    # callReducedGAModel(region)

    # region = 'Tohoku'
    # callReducedGAModel(region)

    # region = 'Kansai'
    # callReducedGAModel(region)


if __name__ == "__main__":
    main()
