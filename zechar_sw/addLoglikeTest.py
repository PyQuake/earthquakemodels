import sys
sys.path.insert(0, '../code')

import models.modelEtasGa as etasGa
import models.model as model
import csep.loglikelihood
import subprocess
import models.randomModel as randomModel
# import applyConvertion2zechar

def addLoglikeTestETAS(modelL, modelO, filename):

	loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
	value = str(("loglikelihood = ", str(loglikeValue)))

	with open(filename, "a") as myfile:
		myfile.write("======")
		myfile.write("\n")
		myfile.write(value)
		myfile.write("\n")
		myfile.write("======")
		myfile.write("\n")
	myfile.close()

def addLoglikeTestGaModel(modelL, modelO, filename):
	
	loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
	value = str(("loglikelihood = ", str(loglikeValue)))

	with open(filename, "a") as myfile:
		myfile.write("======")
		myfile.write("\n")
		myfile.write(value)
		myfile.write("\n")
		myfile.write("======")
		myfile.write("\n")
	myfile.close()

def addingLoglike2Results(year):
	# while year<2010:
	modelL=etasGa.loadModelFromFile('../Zona/model/teste_etasNP'+str(year)+'exec.txt')
	modelO=etasGa.loadModelFromFile('../Zona/realEtas'+str(year)+'.txt')
	addLoglikeTestETAS(modelL, modelO, "gaModels"+str(year)+"/etasNP,R=gaModel+RI-result.txt")

	modelL=model.loadModelFromFile('../Zona/model/teste_modelo'+str(year)+'exec.txt')
	modelO=model.loadModelFromFile('../Zona/real'+str(year)+'.txt')	
	addLoglikeTestETAS(modelL, modelO, "gaModels"+str(year)+"/gaModel,R=etasNP+RI-result.txt")





def testModels(year):
	print(year)
	region="Kansai"
	print(region)
	subprocess.call(['java', '-jar', 'CORSSA Theme VI Tools.jar', 'gaModels'+str(year)+'/'+region+'NP.txt'])
	subprocess.call(['java', '-jar', 'CORSSA Theme VI Tools.jar', 'gaModels'+str(year)+'/'+region+'modelo.txt'])
	region="Kanto"
	print(region)
	subprocess.call(['java', '-jar', 'CORSSA Theme VI Tools.jar', 'gaModels'+str(year)+'/'+region+'NP.txt'])
	subprocess.call(['java', '-jar', 'CORSSA Theme VI Tools.jar', 'gaModels'+str(year)+'/'+region+'modelo.txt'])
	region="Tohoku"
	print(region)
	subprocess.call(['java', '-jar', 'CORSSA Theme VI Tools.jar', 'gaModels'+str(year)+'/'+region+'NP.txt'])
	subprocess.call(['java', '-jar', 'CORSSA Theme VI Tools.jar', 'gaModels'+str(year)+'/'+region+'modelo.txt'])
	region="EastJapan"
	print(region)
	subprocess.call(['java', '-jar', 'CORSSA Theme VI Tools.jar', 'gaModels'+str(year)+'/'+region+'NP.txt'])
	subprocess.call(['java', '-jar', 'CORSSA Theme VI Tools.jar', 'gaModels'+str(year)+'/'+region+'modelo.txt'])

	region="Kansai"
	print(region)
	subprocess.call(['java', '-jar', 'CORSSA Theme VI Tools.jar', 'gaModels'+str(year)+'/'+region+'NP_Hybrid.txt'])
	subprocess.call(['java', '-jar', 'CORSSA Theme VI Tools.jar', 'gaModels'+str(year)+'/'+region+'modelo_Hybrid.txt'])
	region="Kanto"
	print(region)
	subprocess.call(['java', '-jar', 'CORSSA Theme VI Tools.jar', 'gaModels'+str(year)+'/'+region+'NP_Hybrid.txt'])
	subprocess.call(['java', '-jar', 'CORSSA Theme VI Tools.jar', 'gaModels'+str(year)+'/'+region+'modelo_Hybrid.txt'])
	region="Tohoku"
	print(region)
	subprocess.call(['java', '-jar', 'CORSSA Theme VI Tools.jar', 'gaModels'+str(year)+'/'+region+'NP_Hybrid.txt'])
	subprocess.call(['java', '-jar', 'CORSSA Theme VI Tools.jar', 'gaModels'+str(year)+'/'+region+'modelo_Hybrid.txt'])
	region="EastJapan"
	print(region)
	subprocess.call(['java', '-jar', 'CORSSA Theme VI Tools.jar', 'gaModels'+str(year)+'/'+region+'NP_Hybrid.txt'])
	subprocess.call(['java', '-jar', 'CORSSA Theme VI Tools.jar', 'gaModels'+str(year)+'/'+region+'modelo_Hybrid.txt'])
 	

 	# subprocess.call(['java', '-jar', 'CORSSA Theme VI Tools.jar', 'gaModels'+str(year)+'\etasNP,R=gaModel-configFile.txt'])
 	# subprocess.call(['java', '-jar', 'CORSSA Theme VI Tools.jar', 'gaModels'+str(year)+'\gaModel,R=etasNP-configFile.txt'])
 	# addingLoglike2Results(year)


def testControlModels(year):
	modelO=etasGa.loadModelFromFile('../Zona/realEtas'+str(year)+'.txt')	

	randModel = model.newModel(modelO.definitions,False, 1)
	randModel = randomModel.makePoissonModel(randModel)
	randModel.definitions=modelO.definitions
	randModel.definitions[2]['min']=0.0
	etasGa.modelToZecharTests(model=randModel, filename="../Zona/modelTestInZechar/randPoissonModel"+str(year)+".xml",
 		startDate=str(year), endDate=str(year+1))
	subprocess.call(["cp","../Zona/modelTestInZechar/randPoissonModel"+str(year)+".xml", "gaModels"+str(year)+""])
	subprocess.call(['java', '-jar', 'CORSSA Theme VI Tools.jar', './gaModels'+str(year)+'/randPoissonModel'+str(year)+'.txt'])
	addLoglikeTestETAS(randModel, modelO, "gaModels"+str(year)+"/randPoissonModel"+str(year)+"-result.txt")


	tudo1model = model.newModel(modelO.definitions,False, 1)
	tudo1model.definitions=modelO.definitions
	tudo1model.definitions[2]['min']=0.0	
	etasGa.modelToZecharTests(model=tudo1model, filename="../Zona/modelTestInZechar/tudo1model"+str(year)+".xml"
		,startDate=str(year), endDate=str(year+1))
	subprocess.call(["cp","../Zona/modelTestInZechar/tudo1model"+str(year)+".xml", "gaModels"+str(year)+""])
	subprocess.call(['java', '-jar', 'CORSSA Theme VI Tools.jar', 'gaModels'+str(year)+'/tudo1model'+str(year)+'.txt'])
	addLoglikeTestETAS(tudo1model, modelO, "gaModels"+str(year)+"/tudo1model"+str(year)+"-result.txt")



