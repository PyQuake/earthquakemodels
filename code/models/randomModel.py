"""

"""
import numpy.random 
import math
import array
import numpy

def makePoissonModel(model,lam=1):
    """ Modifies the model passed as parameter, replacing all bins 
    with random values taken from a Poisson distribution with lambda = lam

    Returns modified model for chaining"""
    model.bins = (numpy.random.poisson(lam, len(model.bins))+1).tolist()

    return model

def makePoissonModelBinPerBin(model):
    model.prob = (numpy.random.random(size=len(model.bins))).tolist()
    for bin, i in zip(model.prob, range(len(model.bins))):
        model.bins[i] = (numpy.random.poisson(lam=bin))
    return model

def makeRandomModel(model):
    """ Modifies the model passed as parameter, replacing all bins 
    with random values taken from a Random distribution

    Returns modified model for chaining"""
    model.bins = (numpy.random.random(size=len(model.bins))).tolist()

    return model

def arbritaryExtremesModel(model):
    # TODO: calcular o numero de keys in definition
    for i in range(model.definitions[0]['bins']):
        for j in range(model.definitions[1]['bins']):
            model.bins[i*model.definitions[0]['bins']+j]=0
            if i == j :
                model.bins[i*model.definitions[0]['bins']+j]=10
            elif (model.definitions[0]['bins']-1) - i == j:
                model.bins[i*model.definitions[0]['bins']+j]=10
    return model