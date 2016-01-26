import models.modelEtasGa as etasGa
import models.model as model
import csep.loglikelihood

year=2010
region="Tohoku"
for i in range(20):
	'../Zona/paper_exp_2011/EastJapanpaper_etasNP20100.txt'
	modelL=etasGa.loadModelFromFile('../Zona/paper_exp_2011/'+region+'paper_etasNP'+str(year)+str(i)+'.txt')
	modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
	loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
	with open('../Zona/paper_exp_2011/'+region+'paper_etasNP'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
			myfile.write(str(loglikeValue))
			myfile.write("\n")

region="EastJapan"
for i in range(20):
	'../Zona/paper_exp_2011/EastJapanpaper_etasNP20100.txt'
	modelL=etasGa.loadModelFromFile('../Zona/paper_exp_2011/'+region+'paper_etasNP'+str(year)+str(i)+'.txt')
	modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
	loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
	with open('../Zona/paper_exp_2011/'+region+'paper_etasNP'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
			myfile.write(str(loglikeValue))
			myfile.write("\n")

region="kanto"
for i in range(20):
	'../Zona/paper_exp_2011/EastJapanpaper_etasNP20100.txt'
	modelL=etasGa.loadModelFromFile('../Zona/paper_exp_2011/'+region+'paper_etasNP'+str(year)+str(i)+'.txt')
	modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
	loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
	with open('../Zona/paper_exp_2011/'+region+'paper_etasNP'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
			myfile.write(str(loglikeValue))
			myfile.write("\n")

region="Kansai"
for i in range(20):
	'../Zona/paper_exp_2011/EastJapanpaper_etasNP20100.txt'
	modelL=etasGa.loadModelFromFile('../Zona/paper_exp_2011/'+region+'paper_etasNP'+str(year)+str(i)+'.txt')
	modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
	loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
	with open('../Zona/paper_exp_2011/'+region+'paper_etasNP'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
			myfile.write(str(loglikeValue))
			myfile.write("\n")

year=2010
region="Tohoku"
for i in range(20):
	'../Zona/modelo_exp_2011/EastJapanpaper_modelo20100.txt'
	modelL=etasGa.loadModelFromFile('../Zona/paper_exp_2011/'+region+'paper_modelo'+str(year)+str(i)+'.txt')
	modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
	loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
	with open('../Zona/paper_exp_2011/'+region+'paper_modelo'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
			myfile.write(str(loglikeValue))
			myfile.write("\n")

region="EastJapan"
for i in range(20):
	'../Zona/paper_exp_2011/EastJapanpaper_modelo20100.txt'
	modelL=etasGa.loadModelFromFile('../Zona/paper_exp_2011/'+region+'paper_modelo'+str(year)+str(i)+'.txt')
	modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
	loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
	with open('../Zona/paper_exp_2011/'+region+'paper_modelo'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
			myfile.write(str(loglikeValue))
			myfile.write("\n")

region="kanto"
for i in range(20):
	'../Zona/paper_exp_2011/EastJapanpaper_modelo20100.txt'
	modelL=etasGa.loadModelFromFile('../Zona/paper_exp_2011/'+region+'paper_modelo'+str(year)+str(i)+'.txt')
	modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
	loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
	with open('../Zona/paper_exp_2011/'+region+'paper_modelo'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
			myfile.write(str(loglikeValue))
			myfile.write("\n")

region="Kansai"
for i in range(20):
	'../Zona/paper_exp_2011/EastJapanpaper_modelo20100.txt'
	modelL=etasGa.loadModelFromFile('../Zona/paper_exp_2011/'+region+'paper_modelo'+str(year)+str(i)+'.txt')
	modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
	loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
	with open('../Zona/paper_exp_2011/'+region+'paper_modelo'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
			myfile.write(str(loglikeValue))
			myfile.write("\n")