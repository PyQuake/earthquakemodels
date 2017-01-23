#!/usr/bin/env python3
import random
import earthquake.catalog as catalog
import models.model as model
import gaModel.GAModelP_AVR as gaModelP_AVR
import time
import numpy as np


def createRealModelSCwithAMP(
    year, region, qntYears=5, depth=100, withMag=True, save=True):
    definicao = model.loadModelDefinition(
        '../params/' + region + 'Etas_' + str(depth) + '.txt')
    catalog_ = catalog.readFromFile('../data/SC-catalog.dat')
    catalog_ = catalog.filter(catalog_, definicao)
    observation = model.newModel(definicao, mag=False)
    riskMap = catalog.readFromFileP_AVR(
        '../data/Z_JAPAN-AMP-VS400.csv')
    
    riskMap = catalog.filterP_AVR(riskMap, definicao)

    observation = model.addFromCatalogP_AVR(
        observation, catalog_, riskMap, year)
    if save == True:
        model.saveModelToFile(observation,
            '../Zona3/realSCwithAMP/'+ region + 'real' + str(depth) + "_" + str(year) + '.txt', real=True)
    

def execEtasGaModelwithAMP(year, region, depth, qntYears=5, times=10, save=True):
    observations = list()
    means = list()
    for i in range(qntYears):
        observation = model.loadModelFromFile('../Zona3/realSCwithAMP/'
                                  + region + 'real' + str(depth) + "_" + str(year + i) + '.txt')    
        observation.bins = observation.bins.tolist()
        observations.append(observation)
        means.append(observation.bins)
    mean = np.mean(means)

    for i in range(times):
        modelo = gaModelP_AVR.gaModel(
            100,
            500,
            0.9,
            0.1,
            observations,
            year +
            qntYears,
            region,
            mean=mean)
        if save == True:
            model.saveModelToFile(
                modelo,
                '../Zona3/sc-weights/gamodelAMP' +
                'AF' +
                region +
                '_' +
                str(depth) +
                "_" +
                str(
                    year +
                    qntYears) +
                str(i) +
                '.txt')

def callEtasGAModelwithAMP(region ,depth):
    """
    It is a wrapper to the function that generates the list model SC data
    It cover the years of 2000 to 2005, and the models are from 2005 to 2010
    """
    year = 2000
    while(year <= 2005):
        execEtasGaModelwithAMP(year, region, depth)
        year+=1

def main():
    """
    This function creates the needed enviroment needed to generate both GAModel and List Model with SC
    for the regions: EastJapan, Kanto, Kansai, Tohoku
    from 2000 to 2005 to create models from 2005 to 2010
    """
    region = 'Kanto'
    year = 2000
    depth = 100
    while(year <= 2005):
        createRealModelSCwithAMP(year, region, save=True)
        year += 1
    callEtasGAModelwithAMP(region ,depth)

    region = 'EastJapan'
    year = 2000
    depth = 100
    while(year <= 2005):
        createRealModelSCwithAMP(year, region, save=True)
        year += 1
    callEtasGAModelwithAMP(region ,depth)

    region = 'Tohoku'
    year = 2003
    depth = 100
    while(year <= 2005):
        createRealModelSCwithAMP(year, region, save=True)
        year += 1
    callEtasGAModelwithAMP(region ,depth)

    region = 'Kansai'
    year = 2000
    depth = 100
    while(year <= 2005):
        createRealModelSCwithAMP(year, region, save=True)
        year += 1
    callEtasGAModelwithAMP(region ,depth)

if __name__ == "__main__":
    main()
