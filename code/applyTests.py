#depois fazer um arquivo na raiz para rodar todos os testes sobre os modelos
import models.model as model
import csep.loglikelihood as log
import models.randomModel as randomModel

def execTests(year):
	print("Year: ",year)
	print("Loading Model To Test...")
	gaModel=model.loadModelFromFile('../Zona/modelo'+str(year)+'.txt')
	modeloReal=model.loadModelFromFile('../Zona/real'+str(year)+'.txt')	

	print("Applying L-Test and logLikelihood to the gaModel...")
	lTestValue=log.calcLTest(gaModel, modeloReal)
	valueLog=log.calcLogLikelihood(gaModel, modeloReal)
	# lTestValue=log.calcLTest(gaModel, modeloReal, 'perZechar')
	valueN=log.calcNTest(gaModel, modeloReal)
	print("The L Test(perBin) score is: ",lTestValue, "The N Test(perBin) score is: ",valueN, "and the loglikelihood score is: ", valueLog)
	
	randomPoissonModel=model.newModel(modeloReal.definitions)
	randomModel.makePoissonModel(randomPoissonModel)
	print("Applying L-Test to the randomPoissonModel...")
	lTestValue=log.calcLTest(randomPoissonModel, modeloReal)
	valueLog=log.calcLogLikelihood(randomPoissonModel, modeloReal)
	# lTestValue=log.calcLTest(randomPoissonModel, modeloReal, 'perZechar')
	valueN=log.calcNTest(randomPoissonModel, modeloReal)
	print("The L Test(perBin) score is: ",lTestValue, "The N Test(perBin) score is: ",valueN, "and the loglikelihood score is: ", valueLog)

	print("Applying L-Test to the model against itself...")
	lTestValue=log.calcLTest(modeloReal, modeloReal)
	valueLog=log.calcLogLikelihood(modeloReal, modeloReal)
	# lTestValue=log.calcLTest(modeloReal, modeloReal, 'perZechar')
	valueN=log.calcNTest(modeloReal, modeloReal)
	print("The L Test(perBin) score is: ",lTestValue, "The N Test(perBin) score is: ",valueN, "and the loglikelihood score is: ", valueLog)

	nullModel=model.newModel(modeloReal.definitions, 1)
	print("Applying L-Test to the nullModel...")
	lTestValue=log.calcLTest(nullModel, modeloReal)
	valueLog=log.calcLogLikelihood(nullModel, modeloReal)
	# lTestValue=log.calcLTest(nullModel, modeloReal, 'perZechar')
	valueN=log.calcNTest(nullModel, modeloReal)
	print("The L Test(perBin) score is: ",lTestValue, "The N Test(perBin) score is: ",valueN, "and the loglikelihood score is: ", valueLog)

	
		