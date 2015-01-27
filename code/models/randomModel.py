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
            model.bins[i*model.definitions[0]['bins']+j]=1
            if i==0:
                model.bins[i*model.definitions[0]['bins']+j]=numpy.random.poisson()+1
            elif i==44:
                model.bins[i*model.definitions[0]['bins']+j]=numpy.random.poisson()+1
            elif j==0:
                model.bins[i*model.definitions[0]['bins']+j]=numpy.random.poisson()+1
            elif j==44:
                model.bins[i*model.definitions[0]['bins']+j]=numpy.random.poisson()+1

    return model