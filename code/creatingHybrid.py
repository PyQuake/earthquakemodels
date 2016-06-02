import csep.loglikelihood
import gaModel.etasGaModelNP as etasGaModelNP
import models.model as model
import models.modelEtasGa as etasGa

	
def execCreatingHybrid(region, depth, year_begin, year_end):

	year=year_begin
	while(year<=year_end):
		print(year)
		#loading comparative real data
		modelO=model.loadModelFromFile('../Zona2/realData/3.0'+region+'real'+str(depth)+"_"+str(year)+'.txt')
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
			modelO=model.loadModelFromFile('../Zona2/realData/3.0'+region+'real'+str(depth)+"_"+str(year)+'.txt')
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
			modelO=model.loadModelFromFile('../Zona2/realData/3.0'+region+'real'+str(depth)+"_"+str(year)+'.txt')
			modelL.loglikelihood=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
			#saving the hybrid
			etasGa.saveModelToFile(modelL,"../Zona2/hybrid_gaModel/hybrid_gaModel"+region+'_'+str(depth)+'_'+str(year)+'_'+str(i)+".txt")
			# # etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaModelo_Hybrid"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
		year+=1

def execCreatingHybridCLUSTERED(region, depth, year_begin, year_end):

	year=year_begin
	while(year<=year_end):
		print(year)
		#loading comparative real data
		modelO=model.loadModelFromFile('../Zona2/realData/3.0'+region+'real'+str(depth)+"_"+str(year)+'.txt')
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
			modelO=model.loadModelFromFile('../Zona2/realData/3.0'+region+'real'+str(depth)+"_"+str(year)+'.txt')
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
			modelO=model.loadModelFromFile('../Zona2/realData/3.0'+region+'real'+str(depth)+"_"+str(year)+'.txt')
			modelL.loglikelihood=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
			#saving the hybrid
			etasGa.saveModelToFile(modelL,"../Zona2/clustered_hybrid_gaModel/hybrid_gaModel"+region+'_'+str(depth)+'_'+str(year)+'_'+str(i)+".txt")
			# # etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaModelo_Hybrid"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
		year+=1


def main():

	regions = ('Tohoku' ,'EastJapan', 'Kansai', 'Kanto')
	# region = 'EastJapan'
	depths = (25, 60, 100)
	for region in regions:
		print(region)
		for depth in depths:
			print(depth)
	# the year here already is the target year
			execCreatingHybrid(region, depth, 2005, 2010)
			# execCreatingHybridCLUSTERED(region, depth, 2005, 2010)



if __name__ == "__main__":
	main()






