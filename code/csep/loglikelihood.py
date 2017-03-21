"""
Module loglikelihood

performs calculations of Log likelihood of models, following the
definition by Schorlemmer et al. 2007

It also performs the calculations of the LTest and Ntest. Not sure how they work
"""


import sys
import math
import array
import numpy as np
import random
from models.mathUtil import invertPoisson, normalize, percentile

# def logValue(element):
#     if element==0:
#         return 1
#     else:
#         return np.log10(element)

# log = np.vectorize(logValue)
# factorial = np.vectorize(np.math.factorial)    


# Implementation notes:
# Removed "fixing" of lambda = 0 -- this function should not modify models
# Remove the storing of the likelihood for each bin (if necessary may put back)
# Need to test the scores
def calcLogLikelihood(modelLambda, modelOmega):
    """
    Calculates the log likelihood between two RELM models. Lambda is usually
    the forecast model, and Omega is usually the real data model. Both models
    are defined as lists of integers representing earthquake amounts.

    Lambda and Omega must be of the same size.

    If there is a pair of bins lambda/omega, where the lambda bin is 0, and the
    omega bin is not zero, this function will return None
    """
    # global factorial
    
    sumLogLikelihood = 0
    aux=0
    if len(modelLambda.bins) != len(modelOmega.bins):
        raise NameError(
            "Tried to calculate log likelihood for models with different sizes")

    for lambda_i, omega_i in zip(modelLambda.bins, modelOmega.bins):
        if (lambda_i == 0 and omega_i != 0):
            print(lambda_i, omega_i)
            return float('-inf')  # invalid Model

        if (lambda_i == 0 and omega_i == 0):
            sumLogLikelihood += 1
        else:
            sumLogFactorial = 0
            #'factorial' loop
            for i in range(omega_i):
                sumLogFactorial += math.log10(i + 1)
            sumLogLikelihood += -lambda_i + omega_i * \
                math.log10(lambda_i) - sumLogFactorial
    return sumLogLikelihood

# def funcFactorial(element, fact):
#     return fact[element]

# def calcLogLikelihoodNEW(modelLambda, modelOmega,fact):
#     factV = np.vectorize(funcFactorial, excluded=fact)    
#     sumLogLikelihood = np.sum(np.negative(modelLambda.bins) + modelOmega.bins * log(modelLambda.bins) - log(factV(modelOmega.bins, fact)))
#     sumLogLikelihood += np.sum(np.logical_not(np.logical_or(modelLambda.bins,modelOmega.bins)).astype(int))
#     return sumLogLikelihood


def calcLTest(modelLambda, modelOmega):
    """
    Calculates the LTest between the model generated and the model to be compared to.
    The bins of Lambda and Omega must be integer values
    It returns the LTest score between the models Lambda and Omega

    Pros: widely applicable, tests entire forecast
    Cons: blends effects of spatial forecast, rate forecast, magnitude forecast
    """
    # para ca, os modelos devem estar em int, invertPoisson
    lObserved = calcLogLikelihood(modelLambda, modelOmega)

    numberOfSimulations = 1000
    lSimulated = array.array('f')

    for i in range(numberOfSimulations):
        simulatedObservation = type(modelLambda)
        # which type the return of the next function is?? Conversions may be needed
        # it neeed wich king of data in modelLamba.bins? the probability or the integer?
        # by guessing, until now, prob
        # until now, the normalize section i the one that defines it, and I dont know!
        # It is better to send int
        simulatedObservation.bins = simulatedPerBin(modelLambda)
        lSimulated.append(calcLogLikelihood(modelLambda, simulatedObservation))

    gamma = percentile(lObserved, lSimulated)
    return gamma


def simulatedPerBin(modelLambda):
    """
    Generates integer numbers of earthquake from the model Lambda.
    It uses one random value to be used with the probability found at an especific bin of Lambda.
    It should be used to create the simulations need for the loglikelihood based tests.
    """
    bin = []
    rnd = random.random()
    for i in range(len(modelLambda.bins)):
        bin.append(invertPoisson(rnd, modelLambda.bins[i]))
    return bin


# TODO: explain what the NTest is, what it does, and what it measure.
def calcNTest(modelLambda, modelOmega):
    """
    Calculates the NTest between the model generated and the model to be compared to.
    The bins of Lambda and Omega must be integer values
    It returns the NTest score between the models Lambda and Omega

    Pros: isolates rate forecast, widely applicable
    Cons: ignores spatial component, ignores magnitude component
    """

    nObserved = sum(modelLambda.bins)

    numberOfSimulations = 1000
    nSimulated = array.array('i')

    for i in range(numberOfSimulations):
        nSimulated.append(sum(simulatedPerBin(modelLambda)))
    gamma = percentile(nObserved, nSimulated)
    return gamma
