"""

"""
import numpy.random 
import math

def makePoissonModel(model,lam=1):

	model.bins = (numpy.random.poisson(lam, len(model.bins))+1).tolist()

	return model

def poissonPress(x,mi):
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