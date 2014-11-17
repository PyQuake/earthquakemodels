"""
Module loglikelihood

performs calculations of Log likelihood of models, following the 
definition by Schorlemmer et al. 2007
"""

import sys
import math
import array
import numpy.random

from models.randomModel import invertPoisson, normalizeArray


# Implementation notes:
# Removed "fixing" of lambda = 0 -- this function should not modify models
# Remove the storing of the likelihood for each bin (if necessary may put back)
# Need to test the scores
def calcLogLikelihood(modelLambda,modelOmega):
    """
    Calculates the log likelihood between two RELM models. Lambda is usually 
    the forecast model, and Omage is usually the real data model. Both models 
    are defined as lists of integers representing earthquake amounts.
    
    Lambda and Omega must be of the same size.
    
    If there is a pair of bins lambda/omega, where the lambda bin is 0, and the 
    omega bin is not zero, this function will return None
    """

    sumLogLikelihood = 0
    # FIXME: Exception thrown, if it needs a spefic name, we should create an exception class
    #Should abort execution, or sould we continue even after it?
    if len(modelLambda.bins) != len(modelOmega.bins):
        raise NameError("Tried to calculate log likelihood for models with different sizes")

    for lambda_i,omega_i in zip(modelLambda.bins,modelOmega.bins):
        if (lambda_i == 0 and omega_i != 0):
            return float('-inf') # invalid Model	

        if (lambda_i == 0 and omega_i == 0):
            sumLogLikelihood += 1
        else:
            sumLogFactorial = 0
            for i in range(omega_i):
                sumLogFactorial+=math.log10(i+1)
            sumLogLikelihood += -lambda_i + omega_i*math.log10(lambda_i) - sumLogFactorial
            
    return sumLogLikelihood

def calcLTest(modelLambda, modelOmega):
    lObserved = calcLogLikelihood(modelLambda, modelOmega);

    numberOfSimulations = 1000;
    lSimulated = array.array('f')

    for i in range(numberOfSimulations):
        #criar a simulatesEqkCatalog, qual e a entrada??
        simulatedObservation = simulatedEqkCatalog(modelLambda)
        lSimulated.append(calcLogLikelihood(modelLambda,simulatedObservation))

    #criar a percentile
    gamma = MathUtil.percentile(lObserved, lSimulated);
    return gamma

def simulatedEqkCatalog(modelLambda):
    expectedNumberOfEvents = sum(modelLambda.bins);

    # Sample the Poisson distribution with the specified expectation to
    # determine how many events to simulate
    rnd = numpy.random.random()
    
    numberOfEventsToSimulate = invertPoisson(rnd,expectedNumberOfEvents)
    
    # Normalize the expectations so that their sum is unity, use this
    # construct to build the simulated catalog
    #array.array o normalizedExpectations e, tipo 'f'
    cumulativeFractionConstruct=array.array('f')

    normalizedExpectations = normalizeArray(modelLamba.bins);

    cumulativeFractionConstruct=array.array('f')
    cumulativeFractionConstruct.append(normalizedExpectations[0])

    for normalizedExp, cumulativeFraction in zip(normalizedExpectations,cumulativeFractionConstruct):
        if float('inf')!=normalizedExp:
            #need to use cumutaviteFraction i-1
            cumulativeFraction=cumulativeFraction.append(cumulativeFraction[len(cumulativeFraction)-1])+normalizedExp
        else:
            cumutaviteFraction=cumulativeFraction.append(cumulativeFraction[len(cumulativeFraction)-1])

    # Simulate the catalog by drawing random numbers and mapping each
    # random number to a given modelLamba bin, based on its normalized rate
    #should it be short ('h')?? Or if I canged to f as I did, is it ok?
    simulatedObservations=array.array('f')
    for numEvents in numberOfEventsToSimulate:
        rnd = numpy.random.random()
        for j in len(normalizedExpectations):
            if (rnd < cumulativeFractionConstruct[j]):
                simulatedObservations[j]=simulatedObservations[j]+1
                break

    
    return simulatedObservations





