#!/usr/bin/env python3
import sys
sys.path.insert(0, '..')
import random
import earthquake.catalog as catalog
import models.model as model
import gaModel.gaModel_Yuri as ga
import gaModel.etasGaModelNP as etasGaModelNP
import models.modelEtasGa as etasGa
import numpy as np

def createSytheticModel(year, region, depth, withMag=True, save=False):
    """
    Creates a sythetic poisson data model to experiments
    """
    definition = model.loadModelDefinition(
        '../params/' + region + 'Etas_' + str(depth) + '.txt')
    sinteticCatalog = model.newModel(definition)
    sinteticCatalog = randomModel.makeRandomModel(sinteticCatalog)
    sinteticCatalog = randomModel.makePoissonModelBinPerBin(sinteticCatalog)
    # sintetic catalog created
    observations = list()
    observations.append(sinteticCatalog)
    if save == True:
            model.saveModelToFile(
                observation,
                '../Zona3/Sythetic/' +
                str(3.0) +
                region +
                'real' +
                str(depth) +
                "_" +
                str(year) +
                '.txt',
                real=True)


def ExecGASynthetic(region, depth, year=1990, times=5):
    """
    Creates the GAModel with Synthetic catalog
    """
    observations = list()

    for i in range(qntYears):
        observation = model.loadModelFromFile(
            '../Zona3/Sythetic/3.0' + region + 'real' + str(depth) + "_" + str(year + i) + '.txt')
        observation.bins = observation.bins.tolist()
        observations.append(observation)

    for i in range(times):
        modelo = ga.gaModel(
            100,
            0.9,
            0.1,
            observations,
            1990,
            region,
            depth)
        model.saveModelToFile(
            modelo,
            '../Zona2/synthetic/' +
            region +
            '_' +
            str(depth) +
            '.txt')

def ExecEtasGASynthetic(region, depth, year=1990, times=5):
    """
    Creates the list Model with Synthetic catalog
    """
    observations = list()

    for i in range(qntYears):
        observation = model.loadModelFromFile(
            '../Zona3/Sythetic/3.0' + region + 'real' + str(depth) + "_" + str(year + i) + '.txt')
        observation.bins = observation.bins.tolist()
        observations.append(observation)

    for i in range(times):
        modelo = etasGaModelNP.gaModel(
            'non-clustered',
            100,
            0.9,
            0.1,
            observations,
            year,
            region,
            depth)

        etasGa.saveModelToFile(
            modelo,
            '../Zona2/synthetic/' +
            region +
            '_' +
            str(depth) +
            "_" +
            str(year) +
            str(i) +
            '.txt')

def callGAModelSynthetic(region ,depth):
    """
    It is a wrapper to the function that generates the GAModel with synthetic data
    It cover the years of 2000 to 2005, and the models are from 2005 to 2010
    """
    year = 2000
    while(year <= 2005):
        ExecGASynthetic(year, region, depth)
        year+=1


def callEtasGAModelSynthetic(region ,depth):
    """
    It is a wrapper to the function that generates the list model synthetic data
    It cover the years of 2000 to 2005, and the models are from 2005 to 2010
    """
    year = 2000
    while(year <= 2005):
        ExecEtasGASynthetic(year, region, depth)
        year+=1


def main():
    """
    This function creates the needed enviroment needed to generate both GAModel and List Model  with sythetic catalog
    for the regions: EastJapan, Kanto, Kansai, Tohoku
    from 2000 to 2005 to create models from 2005 to 2010
    """
    depth = 100

    region = 'Kanto'
    year = 2000
    while(year <= 2005):
        createRealModelSC(year, region, depth, withMag=True, save=False):
        year += 1
    callEtasGAModelSynthetic(region, depth)
    callGAModelSynthetic(region, depth)

    region = 'EastJapan'
    year = 2000
    while(year <= 2005):
        createRealModelSC(year, region, depth, withMag=True, save=False):
        year += 1
    callEtasGAModelSynthetic(region, depth)
    callGAModelSynthetic(region, depth)


    region = 'Tohoku'
    year = 2000
    while(year <= 2005):
        createRealModelSC(year, region, depth, withMag=True, save=False):
        year += 1
    callEtasGAModelSynthetic(region, depth)
    callGAModelSynthetic(region, depth)

        
    region = 'Kansai'
    year = 2000
    while(year <= 2005):
        createRealModelSC(year, region, depth, withMag=True, save=False):
        year += 1
    callEtasGAModelSynthetic(region, depth)
    callGAModelSynthetic(region, depth)


if __name__ == "__main__":
    main()
