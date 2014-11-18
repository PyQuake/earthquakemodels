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

#TODO: move to math util(?), for sure, we need to take this out of here
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

#TODO: move to math util(?), for sure, we need to take this out of here
def calcNumberBins(lamba_i, omega_i):
    """ Transform a set of real valued bins (0..1) into 
    a set of integer bins, using the value of real data 
    (omega) as the mean for the poisson distribution"""
    for lam,om in zip(lambda_i,omega_i):
        lam = invertPoisson(lam,omega)
    return lamba_i

def normalizeArray(vector):
    #TODO: check if it works with negative values in vector
    arrayCopy=array.array('f')

    sumValue = sum(vector)

    #divide each entry by this sumValue
    for value in vector:
        arrayCopy.append(value/sumValue)

    return arrayCopy

def percentile(value, sample):
    numberOfSamples=len(sample)
    sampleCopy=sample.tolist()
    sampleCopy.sort()
    sampleCopy.reverse()
    print(sampleCopy, value)
    for i in range(numberOfSamples):
        if value<=sampleCopy[i]:
            return float(i/numberOfSamples)
    return 1.0

