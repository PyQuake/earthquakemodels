import models.modelEtasGa as etasGa
import models.model as model
import csep.loglikelihood

year=2006
while(year<=2010):
	print(year)
	region="Tohoku"
	print(region)
	for i in range(10):
		'../Zona/paper_exp/EastJapanpaper_etasNP20100.txt'
		modelL=etasGa.loadModelFromFile('../Zona/paper_exp/'+region+'paper_etasNP'+str(year)+str(i)+'.txt')
		modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
		loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
		with open('../Zona/paper_exp/'+region+'paper_etasNP'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
				myfile.write(str(loglikeValue))
				myfile.write("\n")

	region="EastJapan"
	print(region)
	for i in range(10):
		'../Zona/paper_exp/EastJapanpaper_etasNP20100.txt'
		modelL=etasGa.loadModelFromFile('../Zona/paper_exp/'+region+'paper_etasNP'+str(year)+str(i)+'.txt')
		modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
		loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
		with open('../Zona/paper_exp/'+region+'paper_etasNP'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
				myfile.write(str(loglikeValue))
				myfile.write("\n")

	region="kanto"
	print(region)
	for i in range(10):
		'../Zona/paper_exp/EastJapanpaper_etasNP20100.txt'
		modelL=etasGa.loadModelFromFile('../Zona/paper_exp/'+region+'paper_etasNP'+str(year)+str(i)+'.txt')
		modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
		loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
		with open('../Zona/paper_exp/'+region+'paper_etasNP'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
				myfile.write(str(loglikeValue))
				myfile.write("\n")

	region="Kansai"
	print(region)
	for i in range(10):
		'../Zona/paper_exp/EastJapanpaper_etasNP20100.txt'
		modelL=etasGa.loadModelFromFile('../Zona/paper_exp/'+region+'paper_etasNP'+str(year)+str(i)+'.txt')
		modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
		loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
		with open('../Zona/paper_exp/'+region+'paper_etasNP'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
				myfile.write(str(loglikeValue))
				myfile.write("\n")

	region="Tohoku"
	print(region)
	for i in range(10):
		'../Zona/modelo_exp_2011/EastJapanpaper_modelo20100.txt'
		modelL=etasGa.loadModelFromFile('../Zona/paper_exp/'+region+'paper_modelo'+str(year)+str(i)+'.txt')
		modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
		loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
		with open('../Zona/paper_exp/'+region+'paper_modelo'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
				myfile.write(str(loglikeValue))
				myfile.write("\n")

	region="EastJapan"
	print(region)
	for i in range(10):
		'../Zona/paper_exp/EastJapanpaper_modelo20100.txt'
		modelL=etasGa.loadModelFromFile('../Zona/paper_exp/'+region+'paper_modelo'+str(year)+str(i)+'.txt')
		modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
		loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
		with open('../Zona/paper_exp/'+region+'paper_modelo'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
				myfile.write(str(loglikeValue))
				myfile.write("\n")

	region="kanto"
	print(region)
	for i in range(10):
		'../Zona/paper_exp/EastJapanpaper_modelo20100.txt'
		modelL=etasGa.loadModelFromFile('../Zona/paper_exp/'+region+'paper_modelo'+str(year)+str(i)+'.txt')
		modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
		loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
		with open('../Zona/paper_exp/'+region+'paper_modelo'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
				myfile.write(str(loglikeValue))
				myfile.write("\n")

	region="Kansai"
	print(region)
	for i in range(10):
		'../Zona/paper_exp/EastJapanpaper_modelo20100.txt'
		modelL=etasGa.loadModelFromFile('../Zona/paper_exp/'+region+'paper_modelo'+str(year)+str(i)+'.txt')
		modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
		loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
		with open('../Zona/paper_exp/'+region+'paper_modelo'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
				myfile.write(str(loglikeValue))
				myfile.write("\n")
	year+=1