import random
from models.mathUtil import calcNumberBins

def ass_test(modelLambda, modelOmega):
	"""
	Calculates the ASS value define by Zechar. 
	Its as alarm based test that considers regions, threshold, miss rate and hits.
	The param should be an model with bins that divides one region, and every bin should contain the quatity of earthquakes
	"""
	tau=[]
	for bin in modelLambda.bins:
		tau.append(0)
		rnd=random.random()
		if bin>1:
			tau.append(bin*rnd)
	ass=1-(sum(tau)/sum(modelOmega.bins))
	return ass