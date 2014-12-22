#depois fazer um arquivo na raiz para rodar todos os testes sobre os modelos
import models.model as model
import csep.loglikelihood as log
import models.randomModel as randomModel
import testingAlarmBased.ass as ass
from models.mathUtil import calcNumberBins

def execTests(year):
	print("Year: ",year)
	print("Loading Model To Test...")
	gaModel=model.loadModelFromFile('../Zona/modelo'+str(year)+'.txt')
	modeloReal=model.loadModelFromFile('../Zona/real'+str(year)+'.txt')	

	print("Applying L-Test and logLikelihood to the gaModel...")
	lTestValue=log.calcLTest(gaModel, modeloReal)
	valueLog=log.calcLogLikelihood(gaModel, modeloReal)
	valueN=log.calcNTest(gaModel, modeloReal)
	print("The L Test(perBin) score is: ",lTestValue, "The N Test(perBin) score is: ",valueN, "and the loglikelihood score is: ", valueLog)
	

	randomPoissonModel=model.newModel(modeloReal.definitions)
	randomModel.makePoissonModel(randomPoissonModel)
	randomPoissonModel.bins=calcNumberBins(randomPoissonModel.bins, modeloReal.bins)
	print("Applying L-Test to the randomPoissonModel...")
	lTestValue=log.calcLTest(randomPoissonModel, modeloReal)
	valueLog=log.calcLogLikelihood(randomPoissonModel, modeloReal)
	valueN=log.calcNTest(randomPoissonModel, modeloReal)
	print("The L Test(perBin) score is: ",lTestValue, "The N Test(perBin) score is: ",valueN, "and the loglikelihood score is: ", valueLog)

	print("Applying L-Test to the model against itself...")
	lTestValue=log.calcLTest(modeloReal, modeloReal)
	valueLog=log.calcLogLikelihood(modeloReal, modeloReal)
	valueN=log.calcNTest(modeloReal, modeloReal)
	print("The L Test(perBin) score is: ",lTestValue, "The N Test(perBin) score is: ",valueN, "and the loglikelihood score is: ", valueLog)


	nullModel=model.newModel(modeloReal.definitions, 1)
	randomModel.makePoissonModel(nullModel)
	nullModel.bins=calcNumberBins(nullModel.bins, modeloReal.bins)
	print("Applying L-Test to the nullModel...")
	lTestValue=log.calcLTest(nullModel, modeloReal)
	valueLog=log.calcLogLikelihood(nullModel, modeloReal)
	valueN=log.calcNTest(nullModel, modeloReal)
	print("The L Test(perBin) score is: ",lTestValue, "The N Test(perBin) score is: ",valueN, "and the loglikelihood score is: ", valueLog)

	
def execAss(year):
	gaModel=model.loadModelFromFile('../Zona/modelo'+str(year)+'.txt')
	modeloReal=model.loadModelFromFile('../Zona/real'+str(year)+'.txt')
	
	unskilledModel=model.newModel(modeloReal.definitions)
	randomModel.makeRandomModel(unskilledModel)
	unskilledModel.bins=calcNumberBins(unskilledModel.bins, modeloReal.bins)

	gaModelValue=ass.assTest(gaModel, modeloReal)
	unskilledModelValue=ass.assTest(unskilledModel, modeloReal)

	print(gaModelValue, unskilledModelValue)

def execLTest(year):
	gaModel=model.loadModelFromFile('../Zona/modelo'+str(year)+'.txt')
	modeloReal=model.loadModelFromFile('../Zona/real'+str(year)+'.txt')
	
	unskilledModel=model.newModel(modeloReal.definitions)
	randomModel.makeRandomModel(unskilledModel)
	unskilledModel.bins=calcNumberBins(unskilledModel.bins, modeloReal.bins)

	gaLTestValue=log.calcLTest(gaModel, modeloReal)
	unskilledLTestValue=log.calcLTest(unskilledModel, modeloReal)

	print(galTestValue,unskilledlTestValue)

def execNTest(year):
	gaModel=model.loadModelFromFile('../Zona/modelo'+str(year)+'.txt')
	modeloReal=model.loadModelFromFile('../Zona/real'+str(year)+'.txt')
	
	unskilledModel=model.newModel(modeloReal.definitions)
	randomModel.makeRandomModel(unskilledModel)
	unskilledModel.bins=calcNumberBins(unskilledModel.bins, modeloReal.bins)

	gaNTestValue=log.calcNTest(gaModel, modeloReal)
	unskilledNTestValue=log.calcNTest(unskilledModel, modeloReal)

	print(galTestValue,unskilledlTestValue)

def execLogLikelihood(year):
	gaModel=model.loadModelFromFile('../Zona/modelo'+str(year)+'.txt')
	modeloReal=model.loadModelFromFile('../Zona/real'+str(year)+'.txt')
	
	unskilledModel=model.newModel(modeloReal.definitions)
	randomModel.makeRandomModel(unskilledModel)
	unskilledModel.bins=calcNumberBins(unskilledModel.bins, modeloReal.bins)

	galLLValue=log.calcLogLikelihood(gaModel, modeloReal)
	unskilledLLValue=log.calcLogLikelihood(unskilledModel, modeloReal)

	print(galLLValue,unskilledLLValue)
