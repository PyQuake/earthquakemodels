import csep.loglikelihood
import gaModel.etasGaModelNP as etasGaModelNP
import models.model as model
import models.modelEtasGa as etasGa

	
def execCreatingHybrid(region, depth, year_begin, year_end):

	year=year_begin
	while(year<=year_end):
		print(year)
		#loading comparative real data
		for i in range(10):
			print('executing:', i)
			#loading the list model to be hybrid(ed)...
			modelo=etasGa.loadModelFromFile('../Zona2/listaGA_New/'+region+'_'+str(depth)+'_'+str(year)+str(i)+'.txt')
			#loading mag file...
			fileEtasim="../Zona/paper_exp/etasim1.txt"
			#creating hybrid
			modelL=etasGa.sumTriggeredByDaysWithRI(modelo, year, fileEtasim)
			#adjusting legacy par...
			modelL.mag=True
			#calculating loglike...
			modelO=model.loadModelFromFile('../Zona2/realData/'+region+'real'+"_"+str(year)+'.txt')
			print(type(modelO))
			exit()
			modelL.loglikelihood=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
			#saving the hybrid
			etasGa.saveModelToFile(modelL,"../Zona2/hybrid_ListaGA_New/hybrid_ListaGA_New"+region+'_'+str(depth)+'_'+str(year)+'_'+str(i)+".txt")
			# # etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaNP_Hybrid"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
			#loading the gaModel to be hybrid(ed)...
			modelo=etasGa.loadModelFromFile('../Zona2/gaModel/'+region+'_'+str(depth)+'_'+str(year)+str(i)+'.txt')
			#loading mag file...
			fileEtasim="../Zona/paper_exp/etasim1.txt"
			#creating hybrid
			modelL=etasGa.sumTriggeredByDaysWithRI(modelo, year, fileEtasim)
			#adjusting legacy par...
			modelL.mag=True
			#calculating loglike...
			modelO=model.loadModelFromFile('../Zona2/realData/'+region+'real'+"_"+str(year)+'.txt')
			modelL.loglikelihood=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
			#saving the hybrid
			etasGa.saveModelToFile(modelL,"../Zona2/hybrid_gaModel/hybrid_gaModel"+region+'_'+str(depth)+'_'+str(year)+'_'+str(i)+".txt")
			# # etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaModelo_Hybrid"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
		year+=1

def execCreatingHybridWindow(region, depth, year_begin, year_end):

	year=year_begin
	while(year<=year_end):
		print(year)
		#loading comparative real data
		for i in range(10):
			print('executing:', i)
			#loading the list model to be hybrid(ed)...
			modelo=etasGa.loadModelFromFile('../Zona2/clustered_listaGA_new/'+region+'_'+str(depth)+'_'+str(year)+str(i)+'.txt')
			#loading mag file...
			fileEtasim="../Zona/paper_exp/etasim1.txt"
			#creating hybrid
			modelL=etasGa.sumTriggeredByDaysWithRI(modelo, year, fileEtasim)
			#adjusting legacy par...
			modelL.mag=True
			#calculating loglike...
			modelO=model.loadModelFromFile('../Zona2/realData/'+region+'real'+"_"+str(year)+'.txt')
			modelL.loglikelihood=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
			#saving the hybrid
			etasGa.saveModelToFile(modelL,"../Zona2/clustered_hybrid_ListaGA_New/hybrid_ListaGA_New"+region+'_'+str(depth)+'_'+str(year)+'_'+str(i)+".txt")
			# # etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaNP_Hybrid"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
			#loading the gaModel to be hybrid(ed)...
			modelo=etasGa.loadModelFromFile('../Zona2/clustered_gaModel/'+region+'_'+str(depth)+'_'+str(year)+str(i)+'.txt')
			#loading mag file...
			fileEtasim="../Zona/paper_exp/etasim1.txt"
			#creating hybrid
			modelL=etasGa.sumTriggeredByDaysWithRI(modelo, year, fileEtasim)
			#adjusting legacy par...
			modelL.mag=True
			#calculating loglike...
			modelO=model.loadModelFromFile('../Zona2/realData/'+region+'real'+"_"+str(year)+'.txt')
			modelL.loglikelihood=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
			#saving the hybrid
			etasGa.saveModelToFile(modelL,"../Zona2/clustered_hybrid_gaModel/hybrid_gaModel"+region+'_'+str(depth)+'_'+str(year)+'_'+str(i)+".txt")
			# # etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaModelo_Hybrid"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
		year+=1

def execCreatingHybridSLC(region, depth, year_begin, year_end):

	year=year_begin
	while(year<=year_end):
		print(year)
		#loading comparative real data
		for i in range(10):
			print('executing:', i)
			#loading the list model to be hybrid(ed)...
			modelo=etasGa.loadModelFromFile('../Zona2/clusteredII_listaGA_new/'+region+'_'+str(depth)+'_'+str(year)+str(i)+'.txt')
			#loading mag file...
			fileEtasim="../Zona/paper_exp/etasim1.txt"
			#creating hybrid
			modelL=etasGa.sumTriggeredByDaysWithRI(modelo, year, fileEtasim)
			#adjusting legacy par...
			modelL.mag=True
			#calculating loglike...
			modelO=model.loadModelFromFile('../Zona2/realData/'+region+'real'+"_"+str(year)+'.txt')
			modelL.loglikelihood=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
			#saving the hybrid
			etasGa.saveModelToFile(modelL,"../Zona2/clusteredII_hybrid_ListaGA_New/hybrid_ListaGA_New"+region+'_'+str(depth)+'_'+str(year)+'_'+str(i)+".txt")
			# # etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaNP_Hybrid"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
			#loading the gaModel to be hybrid(ed)...
			modelo=etasGa.loadModelFromFile('../Zona2/clusteredII_gaModel/'+region+'_'+str(depth)+'_'+str(year)+str(i)+'.txt')
			#loading mag file...
			fileEtasim="../Zona/paper_exp/etasim1.txt"
			#creating hybrid
			modelL=etasGa.sumTriggeredByDaysWithRI(modelo, year, fileEtasim)
			#adjusting legacy par...
			modelL.mag=True
			#calculating loglike...
			modelO=model.loadModelFromFile('../Zona2/realData/'+region+'real'+"_"+str(year)+'.txt')
			modelL.loglikelihood=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
			#saving the hybrid
			etasGa.saveModelToFile(modelL,"../Zona2/clusteredII_hybrid_gaModel/hybrid_gaModel"+region+'_'+str(depth)+'_'+str(year)+'_'+str(i)+".txt")
			# # etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaModelo_Hybrid"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
		year+=1

def execCreatingHybridSC(region, depth, year_begin, year_end):

	year=year_begin
	while(year<=year_end):
		print(year)
		#loading comparative real data
		for i in range(10):
			print('executing:', i)
			#loading the list model to be hybrid(ed)...
			modelo=etasGa.loadModelFromFile('../Zona3/scModel/eastgamodel'+region+'_'+str(depth)+'_'+str(year)+str(i)+'.txt')
			#loading mag file...
			fileEtasim="../Zona/paper_exp/etasim1.txt"
			#creating hybrid
			modelL=etasGa.sumTriggeredByDaysWithRI(modelo, year, fileEtasim)
			#adjusting legacy par...
			modelL.mag=True
			#calculating loglike...
			modelO=model.loadModelFromFile('../Zona2/realData/'+region+'real'+"_"+str(year)+'.txt')
			modelL.loglikelihood=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
			#saving the hybrid
			etasGa.saveModelToFile(modelL,"../Zona2/sc_hybrid_ListaGA_New/hybrid_ListaGA_New"+region+'_'+str(depth)+'_'+str(year)+'_'+str(i)+".txt")
			# # etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaNP_Hybrid"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
			
			#loading the gaModel to be hybrid(ed)...
			modelo=etasGa.loadModelFromFile('../Zona3/scModel/gamodel'+region+'_'+str(depth)+'_'+str(year)+str(i)+'.txt')
			#loading mag file...
			fileEtasim="../Zona/paper_exp/etasim1.txt"
			#creating hybrid
			modelL=etasGa.sumTriggeredByDaysWithRI(modelo, year, fileEtasim)
			#adjusting legacy par...
			modelL.mag=True
			#calculating loglike...
			modelO=model.loadModelFromFile('../Zona2/realData/'+region+'real'+"_"+str(year)+'.txt')
			modelL.loglikelihood=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
			#saving the hybrid
			etasGa.saveModelToFile(modelL,"../Zona2/sc_hybrid_gaModel/hybrid_gaModel"+region+'_'+str(depth)+'_'+str(year)+'_'+str(i)+".txt")
			# # etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaModelo_Hybrid"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
		year+=1


def main():

	regions = ('EastJapan', 'Kanto')
	# region = 'EastJapan'
	depth = 100
	for region in regions:
		print(region)
	# the year here already is the target year
		execCreatingHybridSC(region, depth, 2005, 2010)
			# execCreatingHybridWindow(region, depth, 2005, 2010)
			# execCreatingHybridSLC(region, depth, 2005, 2010)



if __name__ == "__main__":
	main()






