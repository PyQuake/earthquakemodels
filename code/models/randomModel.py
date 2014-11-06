"""

"""
import numpy.random 

def makePoissonModel(model,lam=1):

	model.bins = (numpy.random.poisson(lam, len(model.bins))+1).tolist()

	return model