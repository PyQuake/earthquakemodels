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

