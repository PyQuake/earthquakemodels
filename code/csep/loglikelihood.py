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

from models.mathUtil import invertPoisson, normalizeArray, percentile


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

#TODO: explain what the LTest is, what it does, and what it measure.
def calcLTest(modelLambda, modelOmega, simulatingSystem='perBin'):
    """
    Calculates the LTest between the model generated and the model to be compared to. 
    The bins of Lambda and Omega must be probability values
    It returns the LTest score between the models Lambda and Omega
    """ 
    #para ca, os modelos devem estar em int, invertPoisson
    lObserved=calcLogLikelihood(modelLambda, modelOmega)

    numberOfSimulations=1000
    lSimulated=array.array('f')

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
#TODO: Should I make a better explanation of the simulatedPerBin function??
def simulatedPerBin(modelLambda):
    """ 
    Generates integer numbers of earthquake from the model Lambda.
    It uses one random value to be used with the probability found at an especific bin of Lambda.
    It should be used to create the simulations need for the loglikelihood based tests.
    """ 
    bin=[]
    rnd=random.random()
    for i in range(len(modelLambda.bins)):
        bin.append(invertPoisson(rnd, modelLambda.bins[i]))
    return bin

#TODO: Finish it
def simulatedPerZechar(modelLambda):
    """ 
    Not finished
    """ 

    #the function used in Zechar has threshold, though he uses it as 0
    expectedNumberOfEvents=sum(modelLambda.bins)

    # Sample the Poisson distribution with the specified expectation to
    # determine how many events to simulate
    rnd=numpy.random.random()
    
    #this cannot use invertPoisson, or if it can, something is wrong
    #Sure something is wrong, the expectedNumberOfEvents is a interger!
    numberOfEventsToSimulate=invertPoisson(rnd,expectedNumberOfEvents)
    
    # Normalize the expectations so that their sum is unity, use this
    # construct to build the simulated catalog
    #array.array o normalizedExpectations e, tipo 'f'
    #it neeed wich king of data in modelLamba.bins? the probability or the integer?
    #I guess, prob, thought it doesnt kame any sense
    #It is better to receive int
    #modelLambda is not of array type! It list type numpy.asarray, whatever they are the same
    normalizedExpectations=normalizeArray(modelLambda.bins);

    cumulativeFractionConstruct=array.array('f')
    cumulativeFractionConstruct.append(normalizedExpectations[0])

    #this needs testing
    for i in range(len(normalizedExpectations)):
        if float('inf')!=normalizedExpectations[i]:
            #need to use cumutaviteFraction i-1
            cumulativeFractionConstruct.append(cumulativeFractionConstruct[i-1]+normalizedExpectations[i])
        else:
            cumulativeFractionConstruct[i].append(cumulativeFractionConstruct[i-1])

    # Simulate the catalog by drawing random numbers and mapping each
    # random number to a given modelLamba bin, based on its normalized rate
    #should it be short ('h')?? Or if I canged to f as I did, is it ok?
    simulatedObservations=array.array('i')
    for j in range(len(normalizedExpectations)):
        simulatedObservations.append(0)  

    for numEvents in range(numberOfEventsToSimulate):
        rnd = numpy.random.random()
        for j in range(len(normalizedExpectations)):
            if rnd<=cumulativeFractionConstruct[j]:
                # if len(simulatedObservations)<j:
                #     simulatedObservations.append(1)    
                #     break
                # else:
                simulatedObservations[j]=simulatedObservations[j]+1
                break

    
    return simulatedObservations.tolist()


#TODO: explain what the NTest is, what it does, and what it measure.
def calcNTest(modelLambda, modelOmega):
    """
    Calculates the NTest between the model generated and the model to be compared to. 
    The bins of Lambda and Omega must be probability values
    It returns the NTest score between the models Lambda and Omega
    """ 
    #para ca, os modelos devem estar em int, invertPoisson
    nObserved = sum(modelLambda.bins)

    numberOfSimulations = 1000
    nSimulated=array.array('i')

    # simulatedQuantity=[]
    for i in range(numberOfSimulations):
        nSimulated.append(sum(simulatedPerBin(modelLambda)))
        
    gamma=percentile(nObserved, nSimulated)
    return gamma