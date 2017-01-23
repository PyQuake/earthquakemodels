#!/usr/bin/env python3
import sys
sys.path.insert(0, '../code')
import random
import earthquake.catalog as catalog
import models.model as model
import gaModel.GAModelP_AVR as gaModelP_AVR
import time
import numpy as np


def createRealModelSCwithP_AVR(
    year, region, qntYears=5, depth=100, withMag=True, save=True):
    definicao = model.loadModelDefinition(
        '../params/' + region + 'Etas_' + str(depth) + '.txt')
    catalog_ = catalog.readFromFile('../data/SC-catalog.dat')
    catalog_ = catalog.filter(catalog_, definicao)
    observation = model.newModel(definicao, mag=False)
    riskMap = catalog.readFromFileP_AVR(
        '../data/P_AVR-MAP_T30-TTL_TTL_TTL_TOTAL_I45_PS.csv')
    
    riskMap = catalog.filterP_AVR(riskMap, definicao)

    observation = model.addFromCatalogP_AVR(
        observation, catalog_, riskMap, year)
    if save == True:
        model.saveModelToFile(observation,
            '../Zona3/realSCwithP_AVR/' + region + 'real' + str(depth) + "_" + str(year) + '.txt', real=True)
  
def execGaModelwithP_AVR(year, region, depth, qntYears=5, times=10, save=True):
    observations = list()
    means = list()
    for i in range(qntYears):
        observation = model.loadModelFromFile('../Zona3/realSCwithP_AVR/'
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
            mean)
        if save == True:
            model.saveModelToFile(
                modelo,
                '../Zona3/sc-weights/gamodelPSHM/' +
                region +
                '_' +
                str(depth) +
                "_" +
                str(
                    year +
                    qntYears) +
                str(i) +
                '.txt')    


def callGAModelwithP_AVR(region ,depth):
    """
    It is a wrapper to the function that generates the GAModel with SC data
    It cover the years of 2000 to 2005, and the models are from 2005 to 2010
    """
    year = 2000
    while(year <= 2005):
        execEtasGaModelwithP_AVR(year, region, depth)
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
        createRealModelSCwithP_AVR(year, region, save=True)
        year += 1
    callGAModelwithP_AVR(region ,depth)

    region = 'EastJapan'
    year = 2000
    depth = 100
    while(year <= 2005):
        createRealModelSCwithP_AVR(year, region, save=True)
        year += 1
    callGAModelwithP_AVR(region ,depth)

    region = 'Tohoku'
    year = 2003
    depth = 100
    while(year <= 2005):
        createRealModelSCwithP_AVR(year, region, save=True)
        year += 1
    callGAModelwithP_AVR(region ,depth)

    region = 'Kansai'
    year = 2000
    depth = 100
    while(year <= 2005):
        createRealModelSCwithP_AVR(year, region, save=True)
        year += 1
    callGAModelwithP_AVR(region ,depth)

if __name__ == "__main__":
    main()
