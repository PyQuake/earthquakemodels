#!/usr/bin/env python3
import models.mathUtil as mathUtil
import earthquake.catalog as catalog
import models.model as model
import gaModel.gaModel_Yuri as ga
import gaModel.gaModel_YuriWithMag as gaWithMag
import gaModel.etasGaModelNP as etasGaModelNP
import models.modelEtasGa as etasGa
# import sys

def execEtasGaModel(year, region, depth, qntYears=5, times=10, save=True):
	
	observations=list()

	for i in range(qntYears):
		observation=model.loadModelFromFile('../Zona2/realData/3.0'+region+'real'+str(depth)+"_"+str(year+i)+'.txt')
		observation.bins=observation.bins.tolist()
		observations.append(observation)

	for i in range(times):
		modelo=etasGaModelNP.gaModel(100,0.9,0.1,observations, year+qntYears, region)
		modelo.mag=True
		if save==True:
			etasGa.saveModelToFile(modelo, '../Zona2/listaGA_New/'+region+'_'+str(depth)+"_"+str(year+qntYears)+str(i)+'.txt')

def execGaModel(year, region,  depth, qntYears=5, times=10, save=True):

    observations=list()
    
    for i in range(qntYears):
        observation=model.loadModelFromFile('../Zona2/realData/3.0'+region+'real'+str(depth)+"_"+str(year+i)+'.txt')
        observation.bins=observation.bins.tolist()
        observations.append(observation)

    for i in range(times):
        modelo=ga.gaModel(100,0.9,0.1,observations,year+qntYears,region)
        if save==True:
            model.saveModelToFile(modelo, '../Zona2/gaModel/'+region+'_'+str(depth)+"_"+str(year+qntYears)+str(i)+'.txt')

#should not use this one
def execGaModelWithMag(year, region, times, save=False):
	observacao=model.loadModelFromFile('../Zona/realWithMag'+str(year)+'.txt')
	definicao=model.loadModelDefinition('../params/'+region+'WithMag.txt')
	modelo=model.newModel(definicao)
	auxModelo=model.convert2DToArray(modelo, modelo.definitions)
	auxModelo.bins=auxModelo.bins.tolist()
	for i in range(times):
		modelo=ga.gaModel(100,0.9,0.1,auxModelo, year)
		if save==True:
			model.saveModelToFile(model.convertArrayto2D(modelo,definicao), '../Zona/model/modeloWithMag'+str(year)+"exec"+str(i)+'.txt')


def createRealModel(year, region, depth, withMag=True, save=False):
	definicao=model.loadModelDefinition('../params/'+region+'Etas_'+str(depth)+'.txt')
	catalogo=catalog.readFromFile('../data/jmacat_2000_2013.dat')
	catalogo=catalog.filter(catalogo,definicao)
	observacao=model.newModel(definicao, mag=withMag)
	observacao=model.addFromCatalog(observacao,catalogo,year)

	if save==True:
		if observacao.mag==False:
			model.saveModelToFile(observacao, '../Zona2/realData/'+str(3.0)+region+'real'+str(depth)+"_"+str(year)+'.txt', real=True)
		else:
			model.saveModelToFile(observacao, '../Zona/'+region+'realWithMag'+str(year)+'.txt', real=True)

def createRealModelClustered(year, region, depth, withMag=True, save=False):		
	definicao=model.loadModelDefinition('../params/'+region+'Etas_'+str(depth)+'.txt')
	catalogo=catalog.readFromFile('../data/clustered_quakes-M.dat')
	catalogo=catalog.filter(catalogo,definicao)
	observacao=model.newModel(definicao, mag=withMag)
	observacao=model.addFromCatalog(observacao,catalogo,year)

	if save==True:
		if observacao.mag==False:
			model.saveModelToFile(observacao, '../Zona2/clustered/'+str(3.0)+region+'real'+str(depth)+"_"+str(year)+'.txt', real=True)

def execGaModelClustered(year, region,  depth, qntYears=5, times=10, save=True):

    observations=list()
    
    for i in range(qntYears):
        observation=model.loadModelFromFile('../Zona2/clustered/3.0'+region+'real'+str(depth)+"_"+str(year+i)+'.txt')
        observation.bins=observation.bins.tolist()
        observations.append(observation)

    for i in range(times):
        modelo=ga.gaModel(100,0.9,0.1,observations,year+qntYears,region)
        if save==True:
            model.saveModelToFile(modelo, '../Zona2/clustered_gaModel/'+region+'_'+str(depth)+"_"+str(year+qntYears)+str(i)+'.txt')

def execEtasGaModelClustered(year, region, depth, qntYears=5, times=10, save=True):
	
	observations=list()

	for i in range(qntYears):
		observation=model.loadModelFromFile('../Zona2/clustered/3.0'+region+'real'+str(depth)+"_"+str(year+i)+'.txt')
		observation.bins=observation.bins.tolist()
		observations.append(observation)

	for i in range(times):
		modelo=etasGaModelNP.gaModel(100,0.9,0.1,observations, year+qntYears, region)
		modelo.mag=True
		if save==True:
			etasGa.saveModelToFile(modelo, '../Zona2/clustered_listaGA_new/'+region+'_'+str(depth)+"_"+str(year+qntYears)+str(i)+'.txt')


#Actually, in this case, its kind of a mix between withMag and withoutMag
#Hence, we want info about mag, but we are not incorporating it to the data (maybe this will change)
#we need to adapt from both versions
#Not in use, out of date
#should not use this one
def createRealModelforEtas(year, region, depth, save=False):
	definition=model.loadModelDefinition('../params/'+region+'Etas.txt')
	catalogo=catalog.readFromFile('../data/jmacat_2000_2013.dat')
	catalogo=catalog.filter(catalogo,definition)
	observation=etasGa.newModel(definition)
	observation=etasGa.addFromCatalog(observation,catalogo,year)

	observation.mag=True
	if save==True:
		etasGa.saveModelToFile(observation, '../Zona2/'+region+'listaGA_new_'+str(depth)+"_"+str(year)+'.txt', real=True)
	
	return observation

def main():
	year=2000
	while(year<2010):
		print(year)
		# createRealModelClustered(year, region="Tohoku", depth=100, withMag=False, save=True)
		# createRealModelClustered(year, region="Tohoku", depth=25, withMag=False, save=True)
		# createRealModelClustered(year, region="Tohoku", depth=60, withMag=False, save=True)

		# createRealModelClustered(year, region="Tohoku", depth=100, withMag=False, save=True)
		# createRealModelClustered(year, region="Tohoku", depth=25, withMag=False, save=True)
		# createRealModelClustered(year, region="Tohoku", depth=60, withMag=False, save=True)

		# createRealModelClustered(year, region="Kanto", depth=100, withMag=False, save=True)
		# createRealModelClustered(year, region="Kanto", depth=25, withMag=False, save=True)
		# createRealModelClustered(year, region="Kanto", depth=60, withMag=False, save=True)

		# createRealModelClustered(year, region="EastJapan", depth=100, withMag=False, save=True)
		# createRealModelClustered(year, region="EastJapan", depth=25, withMag=False, save=True)
		# createRealModelClustered(year, region="EastJapan", depth=60, withMag=False, save=True)

		# createRealModelClustered(year, region="Kansai", depth=100, withMag=False, save=True)
		# createRealModelClustered(year, region="Kansai", depth=25, withMag=False, save=True)
		# createRealModelClustered(year, region="Kansai", depth=60, withMag=False, save=True)
		# year+=1
		
	# year=2000
	# while(year<2010):
		execEtasGaModelClustered(year, "Tohoku", depth=25, save=True)
		execGaModelClustered(year, "Tohoku", depth=25, save=True)
		execGaModelClustered(year, "Tohoku", depth=60, save=True)
		execEtasGaModelClustered(year, "Tohoku", depth=60, save=True)
		execGaModelClustered(year, "Tohoku", depth=100, save=True)
		execEtasGaModelClustered(year, "Tohoku", depth=100, save=True)
		
	# 	execGaModel(year, "Kanto", depth=25, save=True)
	# 	execEtasGaModel(year, "Kanto", depth=25, save=True)
	# 	execGaModel(year, "Kanto", depth=60, save=True)
	# 	execEtasGaModel(year, "Kanto", depth=60, save=True)
	# 	execGaModel(year, "Kanto", depth=100, save=True)
	# 	execEtasGaModel(year, "Kanto", depth=100, save=True)
		
	# 	execGaModel(year, "EastJapan", depth=25, save=True)
	# 	execEtasGaModel(year, "EastJapan", depth=25, save=True)
	# 	execGaModel(year, "EastJapan", depth=60, save=True)
	# 	execEtasGaModel(year, "EastJapan", depth=60, save=True)
	# 	execGaModel(year, "EastJapan", depth=100, save=True)
	# 	execEtasGaModel(year, "EastJapan", depth=100, save=True)
		
	# 	execGaModel(year, "Kansai", depth=25, save=True)
	# 	execEtasGaModel(year, "Kansai", depth=25, save=True)
	# 	execGaModel(year, "Kansai", depth=60, save=True)
	# 	execEtasGaModel(year, "Kansai", depth=60, save=True)
	# 	execGaModel(year, "Kansai", depth=100, save=True)
	# 	execEtasGaModel(year, "Kansai", depth=100, save=True)

		
		year+=1

if __name__ == "__main__":
	main()
