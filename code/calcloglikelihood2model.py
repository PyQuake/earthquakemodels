import models.modelEtasGa as etasGa
import models.model as model
import csep.loglikelihood

year=2010
# region="Tohoku"
# for i in range(10):
# 	modelL=etasGa.loadModelFromFile('../Zona/paper_exp_2011/'+region+'paper_etasNP'+str(year)+str(i)+'.txt')
# 	modelO=etasGa.loadModelFromFile('../Zona/realEtas'+str(year)+'.txt')
# 	loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
# 	with open('../Zona/paper_exp_2011/'+region+'paper_etasNP'+str(year)+str(i)+'.txt', "w") as myfile:
# 			myfile.write(loglikeValue)
region="EastJapan"
i=0
# for i in range(10):
modelL=etasGa.loadModelFromFile('../Zona/paper_exp_2011/'+region+'paper_etasNP'+str(year)+str(i)+'.txt')
modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
print(loglikeValue)
with open('../Zona/paper_exp_2011/'+region+'paper_etasNP'+str(year)+str(i)+'.txt', "w") as myfile:
		myfile.write(loglikeValue)
# region="kanto"
# for i in range(10):
# 	modelL=etasGa.loadModelFromFile('../Zona/paper_exp_2011/'+region+'paper_etasNP'+str(year)+str(i)+'.txt')
# 	modelO=etasGa.loadModelFromFile('../Zona/realEtas'+str(year)+'.txt')
# 	loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
# 	with open('../Zona/paper_exp_2011/'+region+'paper_etasNP'+str(year)+str(i)+'.txt', "w") as myfile:
# 			myfile.write(loglikeValue)
# region="Kansai"
# for i in range(10):
# 	modelL=etasGa.loadModelFromFile('../Zona/paper_exp_2011/'+region+'paper_etasNP'+str(year)+str(i)+'.txt')
# 	modelO=etasGa.loadModelFromFile('../Zona/realEtas'+str(year)+'.txt')
# 	loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
# 	with open('../Zona/paper_exp_2011/'+region+'paper_etasNP'+str(year)+str(i)+'.txt', "w") as myfile:
# 			myfile.write(loglikeValue)

# modelL=model.loadModelFromFile('../Zona/model/teste_modelo'+str(year)+'exec.txt')
