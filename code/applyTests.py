#depois fazer um arquivo na raiz para rodar todos os testes sobre os modelos
import models.model as model
import csep.loglikelihood as log
import models.randomModel as randomModel
import testingAlarmBased.molchanBased as molchanBased
from models.mathUtil import calcNumberBins
import testingAlarmBased.gamblingScore as gambling

def execTests(year):
	print("Year: ",year)

	f = open("../experiments/"+str(year)+"TestsResults.txt", "w")
        
	gaModel=model.loadModelFromFile('../Zona/modelo'+str(year)+'.txt')
	modeloReal=model.loadModelFromFile('../Zona/real'+str(year)+'.txt')	
	print("Applying all tests available to the gaModel...")
	lTestValue=log.calcLTest(gaModel, modeloReal)
	valueLog=log.calcLogLikelihood(gaModel, modeloReal)
	valueN=log.calcNTest(gaModel, modeloReal)
	molchanValue=molchanBased.molchan(gaModel, modeloReal)
	assValue=molchanBased.assTest(gaModel, modeloReal)
	gamblingScore=gambling.calcGamblingScore(gaModel, modeloReal)
	print("The L Test(perBin) score is: ",lTestValue, "The N Test(perBin) score is: ",valueN, "The Loglikelihood score is: ", valueLog,
	"The molchan Score is: ",molchanValue, "The ASS value is: ", assValue, "The gambling Score is: ", gamblingScore)
	print()
	f.write("gaModel")
	f.write("\n")
	f.write("L Test: "+str(lTestValue))
	f.write("\n")
	f.write("N Test: "+str(valueN))
	f.write("\n")
	f.write("Loglikelihood Test: "+str(valueLog))
	f.write("\n")
	# f.write("Molchan: "+str(molchanValue))
	# f.write("\n")
	f.write("ASS: "+str(assValue))
	f.write("\n")
	f.write("Gambling Score: "+str(gamblingScore))
	f.write("\n")
	f.write("\n")

	randomPoissonModel=model.newModel(modeloReal.definitions)
	randomModel.makePoissonModel(randomPoissonModel)
	print("Applying all tests available to the randomPoissonModel...")
	lTestValue=log.calcLTest(randomPoissonModel, modeloReal)
	valueLog=log.calcLogLikelihood(randomPoissonModel, modeloReal)
	valueN=log.calcNTest(randomPoissonModel, modeloReal)
	molchanValue=molchanBased.molchan(randomPoissonModel, modeloReal)
	assValue=molchanBased.assTest(randomPoissonModel, modeloReal)
	gamblingScore=gambling.calcGamblingScore(randomPoissonModel, modeloReal)
	print("The L Test(perBin) score is: ",lTestValue, "The N Test(perBin) score is: ",valueN, "The Loglikelihood score is: ", valueLog,
	"The molchan Score is: ",molchanValue, "The ASS value is: ", assValue, "The gambling Score is: ", gamblingScore)
	print()
	f.write("randomPoissonModel: ")
	f.write("\n")
	f.write("L Test: "+str(lTestValue))
	f.write("\n")
	f.write("N Test: "+str(valueN))
	f.write("\n")
	f.write("Loglikelihood Test: "+str(valueLog))
	f.write("\n")
	# f.write("Molchan: "+str(molchanValue))
	# f.write("\n")
	f.write("ASS: "+str(assValue))
	f.write("\n")
	f.write("Gambling Score: "+str(gamblingScore))
	f.write("\n")
	f.write("\n")

	print("Applying all tests available to the model against itself...")
	lTestValue=log.calcLTest(modeloReal, modeloReal)
	valueLog=log.calcLogLikelihood(modeloReal, modeloReal)
	valueN=log.calcNTest(modeloReal, modeloReal)
	molchanValue=molchanBased.molchan(modeloReal, modeloReal)
	assValue=molchanBased.assTest(modeloReal, modeloReal)
	gamblingScore=gambling.calcGamblingScore(modeloReal, modeloReal)
	print("The L Test(perBin) score is: ",lTestValue, "The N Test(perBin) score is: ",valueN, "The Loglikelihood score is: ", valueLog,
	"The molchan Score is: ",molchanValue, "The ASS value is: ", assValue, "The gambling Score is: ", gamblingScore)
	print()
	f.write("model against itself: ")
	f.write("\n")
	f.write("L Test: "+str(lTestValue))
	f.write("\n")
	f.write("N Test: "+str(valueN))
	f.write("\n")
	f.write("Loglikelihood Test: "+str(valueLog))
	f.write("\n")
	# f.write("Molchan: "+str(molchanValue))
	# f.write("\n")
	f.write("ASS: "+str(assValue))
	f.write("\n")
	f.write("Gambling Score: "+str(gamblingScore))
	f.write("\n")
	f.write("\n")

	nullModel=model.newModel(modeloReal.definitions, 1)
	print("Applying all tests available to the nullModel...")
	lTestValue=log.calcLTest(nullModel, modeloReal)
	valueLog=log.calcLogLikelihood(nullModel, modeloReal)
	valueN=log.calcNTest(nullModel, modeloReal)
	molchanValue=molchanBased.molchan(nullModel, modeloReal)
	assValue=molchanBased.assTest(nullModel, modeloReal)
	gamblingScore=gambling.calcGamblingScore(nullModel, modeloReal)
	print("The L Test(perBin) score is: ",lTestValue, "The N Test(perBin) score is: ",valueN, "The Loglikelihood score is: ", valueLog,
	"The molchan Score is: ",molchanValue, "The ASS value is: ", assValue, "The gambling Score is: ", gamblingScore)
	print()
	f.write("nullModel")
	f.write("\n")
	f.write("L Test: "+str(lTestValue))
	f.write("\n")
	f.write("N Test: "+str(valueN))
	f.write("\n")
	f.write("Loglikelihood Test: "+str(valueLog))
	f.write("\n")
	# f.write("Molchan: "+str(molchanValue))
	# f.write("\n")
	f.write("ASS: "+str(assValue))
	f.write("\n")
	f.write("Gambling Score: "+str(gamblingScore))
	f.write("\n")
	f.write("\n")

	extremesModel=model.loadModelFromFile('../Zona/extremesModel.txt')
	print("Applying all tests available to the extremesModel...")
	lTestValue=log.calcLTest(extremesModel, modeloReal)
	valueLog=log.calcLogLikelihood(extremesModel, modeloReal)
	valueN=log.calcNTest(extremesModel, modeloReal)
	molchanValue=molchanBased.molchan(extremesModel, modeloReal)
	assValue=molchanBased.assTest(extremesModel, modeloReal)
	gamblingScore=gambling.calcGamblingScore(extremesModel, modeloReal)
	print("The L Test(perBin) score is: ",lTestValue, "The N Test(perBin) score is: ",valueN, "The Loglikelihood score is: ", valueLog,
	"The molchan Score is: ",molchanValue, "The ASS value is: ", assValue, "The gambling Score is: ", gamblingScore)
	print()
	f.write("extremesModel")
	f.write("\n")
	f.write("L Test: "+str(lTestValue))
	f.write("\n")
	f.write("N Test: "+str(valueN))
	f.write("\n")
	f.write("Loglikelihood Test: "+str(valueLog))
	f.write("\n")
	# f.write("Molchan: "+str(molchanValue))
	# f.write("\n")
	f.write("ASS: "+str(assValue))
	f.write("\n")
	f.write("Gambling Score: "+str(gamblingScore))
	f.write("\n")
	f.write("\n")

	f.close()


def execGamblingScore(year):
	gaModel=model.loadModelFromFile('../Zona/modelo'+str(year)+'.txt')
	modeloReal=model.loadModelFromFile('../Zona/real'+str(year)+'.txt')
	
	unskilledModel=model.newModel(modeloReal.definitions)
	randomModel.makeRandomModel(unskilledModel)
	unskilledModel.bins=calcNumberBins(unskilledModel.bins, modeloReal.bins)

	gaGamblingScore=gambling.calcGamblingScore(gaModel, modeloReal)
	unskilledGamblingScore=gambling.calcGamblingScore(unskilledModel, modeloReal)

	print(gaGamblingScore)
	print(unskilledGamblingScore)	

def execAss(year):
	gaModel=model.loadModelFromFile('../Zona/modelo'+str(year)+'.txt')
	modeloReal=model.loadModelFromFile('../Zona/real'+str(year)+'.txt')
	
	unskilledModel=model.newModel(modeloReal.definitions)
	randomModel.makeRandomModel(unskilledModel)
	unskilledModel.bins=calcNumberBins(unskilledModel.bins, modeloReal.bins)

	gaModelValue=molchanBased.assTest(gaModel, modeloReal)
	unskilledModelValue=molchanBased.assTest(unskilledModel, modeloReal)

	print(gaModelValue)
	print(unskilledModelValue)

def execLTest(year):
	gaModel=model.loadModelFromFile('../Zona/modelo'+str(year)+'.txt')
	modeloReal=model.loadModelFromFile('../Zona/real'+str(year)+'.txt')
	
	unskilledModel=model.newModel(modeloReal.definitions)
	randomModel.makeRandomModel(unskilledModel)
	unskilledModel.bins=calcNumberBins(unskilledModel.bins, modeloReal.bins)

	gaLTestValue=log.calcLTest(gaModel, modeloReal)
	unskilledLTestValue=log.calcLTest(unskilledModel, modeloReal)

	print(galTestValue)
	print(unskilledlTestValue)

def execNTest(year):
	gaModel=model.loadModelFromFile('../Zona/modelo'+str(year)+'.txt')
	modeloReal=model.loadModelFromFile('../Zona/real'+str(year)+'.txt')
	
	unskilledModel=model.newModel(modeloReal.definitions)
	randomModel.makeRandomModel(unskilledModel)
	unskilledModel.bins=calcNumberBins(unskilledModel.bins, modeloReal.bins)

	gaNTestValue=log.calcNTest(gaModel, modeloReal)
	unskilledNTestValue=log.calcNTest(unskilledModel, modeloReal)

	print(galTestValue)
	print(unskilledlTestValue)

def execLogLikelihood(year):
	gaModel=model.loadModelFromFile('../Zona/modelo'+str(year)+'.txt')
	modeloReal=model.loadModelFromFile('../Zona/real'+str(year)+'.txt')
	
	unskilledModel=model.newModel(modeloReal.definitions)
	randomModel.makeRandomModel(unskilledModel)
	unskilledModel.bins=calcNumberBins(unskilledModel.bins, modeloReal.bins)

	galLLValue=log.calcLogLikelihood(gaModel, modeloReal)
	unskilledLLValue=log.calcLogLikelihood(unskilledModel, modeloReal)

	print(galLLValue)
	print(unskilledLLValue)

def execTestsbyYear(start=2000, end=2011):
	while(start<=end):
		execTests(start)
		start+=1
