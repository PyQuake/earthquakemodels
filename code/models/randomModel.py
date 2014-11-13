"""

"""
import numpy.random 
import math

def makePoissonModel(model,lam=1):
    """ Modifies the model passed as parameter, replacing all bins 
    with random values taken from a Poisson distribution with lambda = lam

    Returns modified model for chaining"""
	model.bins = (numpy.random.poisson(lam, len(model.bins))+1).tolist()

	return model

def invertPoisson(x,mi):
    """ Calculates the value that would be found in a 
    poisson distribution with lambda = mi at probability
    value X
    """
    if(mi >= 0):
        if(x >= 0):
            if(x < 1):
                l = math.exp(-mi)
                k = 1
                prob = 1 * x
                while(prob>l):
                    k += 1
                    prob = prob * x
                return k

def calcNumberBins(lamba_i, omega_i):
    """ Transform a set of real valued bins (0..1) into 
    a set of integer bins, using the value of real data 
    (omega) as the mean for the poisson distribution"""
    for lam,om in zip(lambda_i,omega_i):
        lam = invertPoisson(lam,omega)
    return lamba_i
