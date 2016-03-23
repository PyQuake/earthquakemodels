import csep.loglikelihood
import gaModel.etasGaModelNP as etasGaModelNP
import models.model as model
import models.modelEtasGa as etasGa

region="Kanto"
year=2006
while(year<=2010):
	modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
	for i in range(10):
		modelo=etasGa.loadModelFromFile('../Zona/paper_exp/'+region+'paper_etasNP'+str(year)+str(i)+'.txt')
		fileEtasim="../Zona/paper_exp/etasim1.txt"
		a=etasGa.sumTriggeredByDaysWithRI(modelo, year, fileEtasim)
		a.mag=True
		a.loglikelihood=csep.loglikelihood.calcLogLikelihood(a,modelO)
		etasGa.saveModelToFile(a,"../Zona/paper_exp/MediaNP_Hybrid"+region+'_'+str(year)+str(i)+"cleaned.txt")
		# etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaNP_Hybrid"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
		modelo=etasGa.loadModelFromFile('../Zona/paper_exp/'+region+'paper_modelo'+str(year)+str(i)+'.txt')
		fileEtasim="../Zona/paper_exp/etasim1.txt"
		a=etasGa.sumTriggeredByDaysWithRI(modelo, year, fileEtasim)
		a.mag=True
		a.loglikelihood=csep.loglikelihood.calcLogLikelihood(a,modelO)
		etasGa.saveModelToFile(a,"../Zona/paper_exp/MediaModelo_Hybrid"+region+'_'+str(year)+str(i)+"cleaned.txt")
		# etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaModelo_Hybrid"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
	year+=1

region="Kansai"
year=2006
while(year<=2010):

	modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
	for i in range(10):
		modelo=etasGa.loadModelFromFile('../Zona/paper_exp/'+region+'paper_etasNP'+str(year)+str(i)+'.txt')
		fileEtasim="../Zona/paper_exp/etasim1.txt"
		a=etasGa.sumTriggeredByDaysWithRI(modelo, year, fileEtasim)
		a.mag=True
		a.loglikelihood=csep.loglikelihood.calcLogLikelihood(a,modelO)
		etasGa.saveModelToFile(a,"../Zona/paper_exp/MediaNP_Hybrid"+region+'_'+str(year)+str(i)+"cleaned.txt")
		# etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaNP_Hybrid"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
		modelo=etasGa.loadModelFromFile('../Zona/paper_exp/'+region+'paper_modelo'+str(year)+str(i)+'.txt')
		fileEtasim="../Zona/paper_exp/etasim1.txt"
		a=etasGa.sumTriggeredByDaysWithRI(modelo, year, fileEtasim)
		a.mag=True
		a.loglikelihood=csep.loglikelihood.calcLogLikelihood(a,modelO)
		etasGa.saveModelToFile(a,"../Zona/paper_exp/MediaModelo_Hybrid"+region+'_'+str(year)+str(i)+"cleaned.txt")
		# etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaModelo_Hybrid"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
	year+=1

region="EastJapan"
year=2006
while(year<=2010):
	modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
	for i in range(10):
		modelo=etasGa.loadModelFromFile('../Zona/paper_exp/'+region+'paper_etasNP'+str(year)+str(i)+'.txt')
		fileEtasim="../Zona/paper_exp/etasim1.txt"
		a=etasGa.sumTriggeredByDaysWithRI(modelo, year, fileEtasim)
		a.mag=True
		a.loglikelihood=csep.loglikelihood.calcLogLikelihood(a,modelO)
		etasGa.saveModelToFile(a,"../Zona/paper_exp/MediaNP_Hybrid"+region+'_'+str(year)+str(i)+"cleaned.txt")
		# etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaNP_Hybrid"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
		modelo=etasGa.loadModelFromFile('../Zona/paper_exp/'+region+'paper_modelo'+str(year)+str(i)+'.txt')
		fileEtasim="../Zona/paper_exp/etasim1.txt"
		a=etasGa.sumTriggeredByDaysWithRI(modelo, year, fileEtasim)
		a.mag=True
		a.loglikelihood=csep.loglikelihood.calcLogLikelihood(a,modelO)
		etasGa.saveModelToFile(a,"../Zona/paper_exp/MediaModelo_Hybrid"+region+'_'+str(year)+str(i)+"cleaned.txt")
		# etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaModelo_Hybrid"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
	year+=1

region="Tohoku"
year=2006
while(year<=2010):
	modelO=etasGa.loadModelFromFile('../Zona/'+region+'realEtas'+str(year)+'.txt')
	for i in range(10):
		modelo=etasGa.loadModelFromFile('../Zona/paper_exp/'+region+'paper_etasNP'+str(year)+str(i)+'.txt')
		fileEtasim="../Zona/paper_exp/etasim1.txt"
		a=etasGa.sumTriggeredByDaysWithRI(modelo, year, fileEtasim)
		a.mag=True
		a.loglikelihood=csep.loglikelihood.calcLogLikelihood(a,modelO)
		etasGa.saveModelToFile(a,"../Zona/paper_exp/MediaNP_Hybrid"+region+'_'+str(year)+str(i)+"cleaned.txt")
		# etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaNP_Hybrid"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
		modelo=etasGa.loadModelFromFile('../Zona/paper_exp/'+region+'paper_modelo'+str(year)+str(i)+'.txt')
		fileEtasim="../Zona/paper_exp/etasim1.txt"
		a=etasGa.sumTriggeredByDaysWithRI(modelo, year, fileEtasim)
		a.mag=True
		a.loglikelihood=csep.loglikelihood.calcLogLikelihood(a,modelO)
		etasGa.saveModelToFile(a,"../Zona/paper_exp/MediaModelo_Hybrid"+region+'_'+str(year)+str(i)+"cleaned.txt")
		# etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaModelo_Hybrid"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
	year+=1
	