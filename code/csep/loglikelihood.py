"""
Module loglikelihood

performs calculations of Log likelihood of models, following the 
definition by Schorlemmer et al. 2007
"""

import sys
import math
import array
import numpy
import random

from models.randomModel import invertPoisson, normalizeArray, percentile


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

def calcLTest(modelLambda, modelOmega, simulatingSystem='perBin'):
    #para ca, os modelos devem estar em int, invertPoisson
    lObserved = calcLogLikelihood(modelLambda, modelOmega);

    numberOfSimulations = 1000
    lSimulated = array.array('f')

    for i in range(numberOfSimulations):
        simulatedObservation=type(modelLambda)
        #which type the return of the next function is?? Conversions may be needed
        #it neeed wich king of data in modelLamba.bins? the probability or the integer?
        #by guessing, until now, prob
        #until now, the normalize section i the one that defines it, and I dont know!
        #It is better to send int
        if(simulatingSystem=='perZechar'):
            simulatedObservation.bins = simulatedPerZechar(modelLambda)
        elif(simulatingSystem=='perBin'):
            simulatedObservation.bins = simulatedPerBin(modelLambda)

        lSimulated.append(calcLogLikelihood(modelLambda,simulatedObservation))

    gamma=percentile(lObserved, lSimulated)
    return gamma

#why does it add so big numbers????
def simulatedPerBin(modelLambda):
    bin = []
    for i in range(len(modelLambda.bins)):
        #poisson ou random mesmo?
        rnd=random.random()
        #usar o modelLambda.bins??
        bin.append(invertPoisson(rnd, modelLambda.bins[i]))
    return bin

#TODO: Finish it
def simulatedPerZechar(modelLambda):
    #the function used in Zechar has threshold, though he uses it as 0
    expectedNumberOfEvents = sum(modelLambda.bins)

    # Sample the Poisson distribution with the specified expectation to
    # determine how many events to simulate
    rnd = numpy.random.random()
    
    #this cannot use invertPoisson, or if it can, something is wrong
    #Sure something is wrong, the expectedNumberOfEvents is a interger!
    numberOfEventsToSimulate = invertPoisson(rnd,expectedNumberOfEvents)
    
    # Normalize the expectations so that their sum is unity, use this
    # construct to build the simulated catalog
    #array.array o normalizedExpectations e, tipo 'f'
    #it neeed wich king of data in modelLamba.bins? the probability or the integer?
    #I guess, prob, thought it doesnt kame any sense
    #It is better to receive int
    #modelLambda is not of array type! It list type numpy.asarray, whatever they are the same
    normalizedExpectations = normalizeArray(modelLamba.bins);

    cumulativeFractionConstruct=array.array('f')
    cumulativeFractionConstruct.append(normalizedExpectations[0])

    #this needs testing
    for i in range(len(normalizedExpectations)):
        if float('inf')!=normalizedExp:
            #need to use cumutaviteFraction i-1
            cumulativeFractionConstruct[i]=cumulativeFractionConstruct[i-1]+normalizedExp
        else:
            cumulativeFractionConstruct[i]=cumulativeFractionConstruct[i-1]

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

    
    return simulatedObservations.tolist()





