import sys
sys.path.insert(0, '../code')

from csep.loglikelihood import calcLogLikelihood, calcLogLikelihoodNEW
from models.mathUtil import calcNumberBins, calcNumberBinsOld, loadFactorial
import numpy as np
import models.model as model
#input: two probabilistic vectors
def test_calcNumberBins(input1, input2):
	newValue = calcNumberBins(input1, input2)
	oldValue = calcNumberBinsOld(input1, input2)
	return newValue==oldValue

def testeLogLikelihood(input1, input2):
	fact = loadFactorial('../data/factorial.txt')
	
	definition = model.loadModelDefinition('../params/Kanto.txt')
	var1 = model.newModel(definition)
	var2 = model.newModel(definition)

	var1.bins = input1
	var2.bins = input2
	newValue = calcLogLikelihoodNEW(var1, var2, fact)
	oldValue = calcLogLikelihood(var1, var2)
	print(newValue, oldValue)
	return newValue==oldValue

def main():
	var1 = np.array([0,0,0,0,0,0,0,0])
	var2 = np.array([0,0,0,0,0,0,0,0])
	print(test_calcNumberBins(var1, var2))

	var1 = np.array([0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01])
	var2 = np.array([1,1,1,1,1,1,1,1])
	print(test_calcNumberBins(var1, var2))

	var1 = np.array([0.12,0.01,0.9,0.09678,0.321,0.178,0.03,0.5])
	var2 = np.array([1,1,1,1,1,1,1,1])
	print(test_calcNumberBins(var1, var2))
	
	var1 = np.array([0.12,0.01,0.9,0.09678,0.321,0.178,0.03,0.5])
	var2 = np.array([1,6,9,5,1,3,1,2])
	print(test_calcNumberBins(var1, var2))



	var1 = np.array([0,0,0,0,0,0,0,0])
	var2 = np.array([0,0,0,0,0,0,0,0])
	print(testeLogLikelihood(var1, var2))

	var1 = np.array([1,1,1,1,1,1,1,1])
	var2 = np.array([1,1,1,1,1,1,1,1])
	print(testeLogLikelihood(var1, var2))

	var1 = np.array([1,6,9,5,1,3,1,2])
	var2 = np.array([1,1,1,1,1,1,1,1])
	print(testeLogLikelihood(var1, var2))
	
	var1 = np.array([12,1,9,9678,321,178,3,5])
	var2 = np.array([1,6,9,5,1,3,1,2])
	print(testeLogLikelihood(var1, var2))




if __name__ == "__main__":
	main()
