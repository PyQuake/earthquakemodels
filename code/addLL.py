import models.modelEtasGa as etasGa
import models.model as model
import csep.loglikelihood

# year=2006
# while(year<=2010):
# 	print(year)
# 	region="Tohoku"
# 	print(region)
# 	for i in range(10):
# 		'../Zona/paper_exp/EastJapanpaper_etasNP20100.txt'
# 		modelL=etasGa.loadModelFromFile('../Zona/paper_exp/'+region+'paper_etasNP'+str(year)+str(i)+'.txt')
# 		modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
# 		loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
# 		with open('../Zona/paper_exp/'+region+'paper_etasNP'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
# 				myfile.write(str(loglikeValue))
# 				myfile.write("\n")

# 	region="EastJapan"
# 	print(region)
# 	for i in range(10):
# 		'../Zona/paper_exp/EastJapanpaper_etasNP20100.txt'
# 		modelL=etasGa.loadModelFromFile('../Zona/paper_exp/'+region+'paper_etasNP'+str(year)+str(i)+'.txt')
# 		modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
# 		loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
# 		with open('../Zona/paper_exp/'+region+'paper_etasNP'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
# 				myfile.write(str(loglikeValue))
# 				myfile.write("\n")

# 	region="kanto"
# 	print(region)
# 	for i in range(10):
# 		'../Zona/paper_exp/EastJapanpaper_etasNP20100.txt'
# 		modelL=etasGa.loadModelFromFile('../Zona/paper_exp/'+region+'paper_etasNP'+str(year)+str(i)+'.txt')
# 		modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
# 		loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
# 		with open('../Zona/paper_exp/'+region+'paper_etasNP'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
# 				myfile.write(str(loglikeValue))
# 				myfile.write("\n")

# 	region="Kansai"
# 	print(region)
# 	for i in range(10):
# 		'../Zona/paper_exp/EastJapanpaper_etasNP20100.txt'
# 		modelL=etasGa.loadModelFromFile('../Zona/paper_exp/'+region+'paper_etasNP'+str(year)+str(i)+'.txt')
# 		modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
# 		loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
# 		with open('../Zona/paper_exp/'+region+'paper_etasNP'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
# 				myfile.write(str(loglikeValue))
# 				myfile.write("\n")

# 	region="Tohoku"
# 	print(region)
# 	for i in range(10):
# 		'../Zona/modelo_exp_2011/EastJapanpaper_modelo20100.txt'
# 		modelL=etasGa.loadModelFromFile('../Zona/paper_exp/'+region+'paper_modelo'+str(year)+str(i)+'.txt')
# 		modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
# 		loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
# 		with open('../Zona/paper_exp/'+region+'paper_modelo'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
# 				myfile.write(str(loglikeValue))
# 				myfile.write("\n")

# 	region="EastJapan"
# 	print(region)
# 	for i in range(10):
# 		'../Zona/paper_exp/EastJapanpaper_modelo20100.txt'
# 		modelL=etasGa.loadModelFromFile('../Zona/paper_exp/'+region+'paper_modelo'+str(year)+str(i)+'.txt')
# 		modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
# 		loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
# 		with open('../Zona/paper_exp/'+region+'paper_modelo'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
# 				myfile.write(str(loglikeValue))
# 				myfile.write("\n")

# 	region="kanto"
# 	print(region)
# 	for i in range(10):
# 		'../Zona/paper_exp/EastJapanpaper_modelo20100.txt'
# 		modelL=etasGa.loadModelFromFile('../Zona/paper_exp/'+region+'paper_modelo'+str(year)+str(i)+'.txt')
# 		modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
# 		loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
# 		with open('../Zona/paper_exp/'+region+'paper_modelo'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
# 				myfile.write(str(loglikeValue))
# 				myfile.write("\n")

# 	region="Kansai"
# 	print(region)
# 	for i in range(10):
# 		'../Zona/paper_exp/EastJapanpaper_modelo20100.txt'
# 		modelL=etasGa.loadModelFromFile('../Zona/paper_exp/'+region+'paper_modelo'+str(year)+str(i)+'.txt')
# 		modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
# 		loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
# 		with open('../Zona/paper_exp/'+region+'paper_modelo'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
# 				myfile.write(str(loglikeValue))
# 				myfile.write("\n")
# 	year+=1


def addLoglike2(region, depth, year_begin, year_end):

	year=year_begin
	while(year<=year_end):
		print(year)
		for i in range(10):
			modelL=etasGa.loadModelFromFile('../Zona2/gaModel/'+region+'_'+str(depth)+'_'+str(year)+str(i)+'.txt')
			modelO=observation=model.loadModelFromFile('../Zona2/realData/3.0'+region+'real'+str(depth)+"_"+str(year)+'.txt')
			loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
			with open('../Zona2/gaModel/'+region+'_'+str(depth)+'_'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
					myfile.write(str(loglikeValue))
					myfile.write("\n")
		year+=1

def main():
	#the year here already is the target year
	addLoglike2('Tohoku', 25, 2005, 2010)
	addLoglike2('Tohoku', 60, 2005, 2010)
	addLoglike2('Tohoku', 100, 2005, 2010)

	addLoglike2('EastJapan', 25, 2005, 2010)
	addLoglike2('EastJapan', 60, 2005, 2010)
	addLoglike2('EastJapan', 100, 2005, 2010)

	addLoglike2('Kanto', 25, 2005, 2010)
	addLoglike2('Kanto', 60, 2005, 2010)
	addLoglike2('Kanto', 100, 2005, 2010)

	addLoglike2('Kansai', 25, 2005, 2010)
	addLoglike2('Kansai', 60, 2005, 2010)
	addLoglike2('Kansai', 100, 2005, 2010)

if __name__ == "__main__":
	main()