"""
Module loglikelihood

performs calculations of Log likelihood of models, following the 
definition by Schorlemmer et al. 2007
"""

import sys
import math

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
    # FIXME: this probably should throw an exception instead.
    if len(modelLambda) != len(modelOmega):
        sys.exit("Tried to calculate log likelihood for models with different sizes")

    for lambda_i,omega_i in zip(modelLambda,modelOmega):
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


