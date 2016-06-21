import numpy as np
from scipy.optimize import minimize
# import scipy
import models.mathUtil as mathUtil
import models.model as model
from csep.loglikelihood import calcLogLikelihood as loglikelihood

region= 'EastJapan'
year=2000
depth=25

modelOmega=list()

qntYears = 5
for i in range(qntYears):
    observation=model.loadModelFromFile('../Zona2/realData/3.0'+region+'real'+str(depth)+"_"+str(year+i)+'.txt')
    observation.bins=observation.bins.tolist()
    modelOmega.append(observation)


def evaluationFunction(individual):
	
	logValue = float('Infinity')
	modelLambda=type(modelOmega[0])
	for i in range(len(modelOmega)):
		modelLambda.bins=individual
		tempValue=loglikelihood(modelLambda, modelOmega[i])

		if tempValue < logValue:
			logValue = tempValue
	return logValue



a = np.random.randint(low=10, high=22, size=len(modelOmega[0].bins))
x0 = a.tolist()
# res = minimize(evaluationFunction, x0, method='Nelder-Mead', tol=1e-1)
res = minimize(evaluationFunction, x0, method='BFGS', jac=False,options={'gtol': 1e-6, 'disp': True})
print(res.x, res.message)