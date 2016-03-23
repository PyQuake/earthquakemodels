import models.modelEtasGa as etasGa
import models.model as model
import csep.loglikelihood

year=2006
while(year<=2010):
	print(year)
	region="Tohoku"
	print(region)
	for i in range(10):
		modelL=etasGa.loadModelFromFile("../Zona/paper_exp/MediaNP_Hybrid"+region+'_'+str(year)+str(i)+"cleaned.txt")
		modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
		loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
		with open('../Zona/paper_exp/Hybrid'+region+'paper_etasNP'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
				myfile.write(str(loglikeValue))
				myfile.write("\n")

	region="EastJapan"
	print(region)
	for i in range(10):
		modelL=etasGa.loadModelFromFile("../Zona/paper_exp/MediaNP_Hybrid"+region+'_'+str(year)+str(i)+"cleaned.txt")
		modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
		loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
		with open('../Zona/paper_exp/Hybrid'+region+'paper_etasNP'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
				myfile.write(str(loglikeValue))
				myfile.write("\n")

	region="kanto"
	print(region)
	for i in range(10):
		modelL=etasGa.loadModelFromFile("../Zona/paper_exp/MediaNP_Hybrid"+region+'_'+str(year)+str(i)+"cleaned.txt")
		modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
		loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
		with open('../Zona/paper_exp/Hybrid'+region+'paper_etasNP'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
				myfile.write(str(loglikeValue))
				myfile.write("\n")

	region="Kansai"
	print(region)
	for i in range(10):
		modelL=etasGa.loadModelFromFile("../Zona/paper_exp/MediaNP_Hybrid"+region+'_'+str(year)+str(i)+"cleaned.txt")
		modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
		loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
		with open('../Zona/paper_exp/Hybrid'+region+'paper_etasNP'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
				myfile.write(str(loglikeValue))
				myfile.write("\n")

	region="Tohoku"
	print(region)
	for i in range(10):
		modelL=etasGa.loadModelFromFile("../Zona/paper_exp/MediaModelo_Hybrid"+region+'_'+str(year)+str(i)+"cleaned.txt")
		modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
		loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
		with open('../Zona/paper_exp/Hybrid'+region+'paper_modelo'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
				myfile.write(str(loglikeValue))
				myfile.write("\n")

	region="EastJapan"
	print(region)
	for i in range(10):
		modelL=etasGa.loadModelFromFile("../Zona/paper_exp/MediaModelo_Hybrid"+region+'_'+str(year)+str(i)+"cleaned.txt")
		modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
		loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
		with open('../Zona/paper_exp/Hybrid'+region+'paper_modelo'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
				myfile.write(str(loglikeValue))
				myfile.write("\n")

	region="kanto"
	print(region)
	for i in range(10):
		modelL=etasGa.loadModelFromFile("../Zona/paper_exp/MediaModelo_Hybrid"+region+'_'+str(year)+str(i)+"cleaned.txt")
		modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
		loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
		with open('../Zona/paper_exp/Hybrid'+region+'paper_modelo'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
				myfile.write(str(loglikeValue))
				myfile.write("\n")

	region="Kansai"
	print(region)
	for i in range(10):
		modelL=etasGa.loadModelFromFile("../Zona/paper_exp/MediaModelo_Hybrid"+region+'_'+str(year)+str(i)+"cleaned.txt")
		modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
		loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
		with open('../Zona/paper_exp/Hybrid'+region+'paper_modelo'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
				myfile.write(str(loglikeValue))
				myfile.write("\n")
	year+=1