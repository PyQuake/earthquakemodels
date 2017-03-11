#!/usr/bin/env python3
import sys
sys.path.insert(0, '..')
import earthquake.catalog as catalog
import models.model as model

def createRealModel(year, region):
    """
    Creates the real data model with SC catalog to experiments
    """
    realModel = model.loadModelDB(region+'jmaData', year)
    
    definition = model.loadModelDefinition('../../params/' + region + '.txt')
    if (realModel.definitions==None):
        catalog_ = catalog.readFromFile('../../data/jmacat_2000_2013.dat')
        catalog_ = catalog.filter(catalog_, definition)
        observation = model.newModel(definition)
        observation = model.addFromCatalog(observation, catalog_, year)
        observation.modelName = region+'jmaData' 
        model.saveModelDB(observation)

def main():
    region = 'Kanto'
    year = 2000
    while(year <= 2013):
        createRealModel(year, region)
        year += 1

    region = 'EastJapan'
    year = 2000
    while(year <= 2013):
        createRealModel(year, region)
        year += 1

    region = 'Kansai'
    year = 2000
    while(year <= 2013):
        createRealModel(year, region)
        year += 1

    region = 'Tohoku'
    year = 2000
    while(year <= 2013):
        createRealModel(year, region)
        year += 1


if __name__ == "__main__":
    main()
