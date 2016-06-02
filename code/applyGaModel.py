#!/usr/bin/env python3
import models.mathUtil as mathUtil
import earthquake.catalog as catalog
import models.model as model
import gaModel.gaModel_Yuri as ga
import gaModel.gaModel_YuriWithMag as gaWithMag
import gaModel.etasGaModelNP as etasGaModelNP
import models.modelEtasGa as etasGa
import models.randomModel as randomModel

def execEtasGaModel(year, region, depth, qntYears=5, times=10, save=True):
	
	observations=list()

	for i in range(qntYears):
		observation=model.loadModelFromFile('../Zona2/realData/3.0'+region+'real'+str(depth)+"_"+str(year+i)+'.txt')
		observation.bins=observation.bins.tolist()
		observations.append(observation)

	for i in range(times):
		modelo=etasGaModelNP.gaModel('non-clustered', 100,0.9,0.1,observations, year+qntYears, region, depth)
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
        modelo=ga.gaModel('non-clustered', 100,0.9,0.1,observations,year+qntYears,region, depth)
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
		modelo=ga.gaModel('non-clustered', 100,0.9,0.1,auxModelo, year)
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
	observacao=model.addFromCatalog(observacao,catalogo,year,)

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
        modelo=ga.gaModel('clustered', 100,0.9,0.1,observations,year+qntYears,region, depth)
        if save==True:
            model.saveModelToFile(modelo, '../Zona2/clustered_gaModel/'+region+'_'+str(depth)+"_"+str(year+qntYears)+str(i)+'.txt')

def execEtasGaModelClustered(year, region, depth, qntYears=5, times=10, save=True):
	
	observations=list()

	for i in range(qntYears):
		observation=model.loadModelFromFile('../Zona2/clustered/3.0'+region+'real'+str(depth)+"_"+str(year+i)+'.txt')
		observation.bins=observation.bins.tolist()
		observations.append(observation)

	for i in range(times):
		modelo=etasGaModelNP.gaModel('clustered', 100,0.9,0.1,observations, year+qntYears, region, depth)
		modelo.mag=True
		if save==True:
			etasGa.saveModelToFile(modelo, '../Zona2/clustered_listaGA_new/'+region+'_'+str(depth)+"_"+str(year+qntYears)+str(i)+'.txt')

def createRealModelClusteredII(year, region, depth, withMag=True, save=False):		
	definicao=model.loadModelDefinition('../params/'+region+'Etas_'+str(depth)+'.txt')
	catalogo=catalog.readFromFile('../data/regions_classified-M.dat')
	catalogo=catalog.filter(catalogo,definicao)
	observacao=model.newModel(definicao, mag=withMag)
	observacao=model.addFromCatalog(observacao,catalogo,year,)

	if save==True:
		if observacao.mag==False:
			model.saveModelToFile(observacao, '../Zona2/clusteredII/'+str(3.0)+region+'real'+str(depth)+"_"+str(year)+'.txt', real=True)


def execGaModelClusteredII(year, region,  depth, qntYears=5, times=10, save=True):

    observations=list()
    
    for i in range(qntYears):
        observation=model.loadModelFromFile('../Zona2/clusteredII/3.0'+region+'real'+str(depth)+"_"+str(year+i)+'.txt')
        observation.bins=observation.bins.tolist()
        observations.append(observation)

    for i in range(times):
        modelo=ga.gaModel('clusteredII', 100,0.9,0.1,observations,year+qntYears,region, depth)
        if save==True:
            model.saveModelToFile(modelo, '../Zona2/clusteredII_gaModel/'+region+'_'+str(depth)+"_"+str(year+qntYears)+str(i)+'.txt')

def execEtasGaModelClusteredII(year, region, depth, qntYears=5, times=10, save=True):
	
	observations=list()

	for i in range(qntYears):
		observation=model.loadModelFromFile('../Zona2/clusteredII/3.0'+region+'real'+str(depth)+"_"+str(year+i)+'.txt')
		observation.bins=observation.bins.tolist()
		observations.append(observation)

	for i in range(times):
		modelo=etasGaModelNP.gaModel('clusteredII', 100,0.9,0.1,observations, year+qntYears, region, depth)
		modelo.mag=True
		if save==True:
			etasGa.saveModelToFile(modelo, '../Zona2/clusteredII_listaGA_new/'+region+'_'+str(depth)+"_"+str(year+qntYears)+str(i)+'.txt')


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

def createAndExeGASynthetic(region, depth, year=1990,times=5):
	definicao=model.loadModelDefinition('../params/'+region+'Etas_'+str(depth)+'.txt')
	sinteticCatalog=model.newModel(definicao)
	sinteticCatalog=randomModel.makeRandomModel(sinteticCatalog)
	sinteticCatalog=randomModel.makePoissonModelBinPerBin(sinteticCatalog)
	#sintetic catalog created
	observations = list()
	observations.append(sinteticCatalog)

	for i in range(times):
		modelo=ga.gaModel('synthetic', 100,0.9,0.1,observations,1990,region, depth)
		model.saveModelToFile(modelo, '../Zona2/synthetic/'+region+'_'+str(depth)+'.txt')

	for i in range(times):
		modelo=etasGaModelNP.gaModel('non-clustered', 100,0.9,0.1,observations, year, region, depth)
		modelo.mag=True
		etasGa.saveModelToFile(modelo, '../Zona2/synthetic/'+region+'_'+str(depth)+"_"+str(year)+str(i)+'.txt')

def main():
	# createAndExeGASynthetic('Kanto', 100)
	# createAndExeGASynthetic('Kanto', 60)
	# createAndExeGASynthetic('Kanto', 25)
	# exec real model
	# year=2000
	# while(year<2011):
	# 	regions = ('Tohoku' ,'EastJapan', 'Kansai', 'Kanto')
	# 	for region in regions:
	# 		createRealModelClusteredII(year, region=region, depth=60, withMag=False, save=True)
	# 		createRealModelClusteredII(year, region=region, depth=100, withMag=False, save=True)
	# 		createRealModelClusteredII(year, region=region, depth=25, withMag=False, save=True)
	# # 	print(year, 'Tohoku')
	# # 	createRealModel(year, region="Tohoku", depth=100, withMag=False, save=True)
	# # 	createRealModel(year, region="Tohoku", depth=25, withMag=False, save=True)
	# # 	createRealModel(year, region="Tohoku", depth=60, withMag=False, save=True)
	# # 	print('Kanto')
	# # 	createRealModel(year, region="Kanto", depth=100, withMag=False, save=True)
	# 	# createRealModel(year, region="Kanto", depth=25, withMag=False, save=True)
	# 	# createRealModel(year, region="Kanto", depth=60, withMag=False, save=True)
	# # 	print('eastjapan')
	# # 	createRealModel(year, region="EastJapan", depth=100, withMag=False, save=True)
	# # 	createRealModel(year, region="EastJapan", depth=25, withMag=False, save=True)
	# # 	createRealModel(year, region="EastJapan", depth=60, withMag=False, save=True)
	# # 	print('kansai')
	# # 	createRealModel(year, region="Kansai", depth=100, withMag=False, save=True)
	# # 	createRealModel(year, region="Kansai", depth=25, withMag=False, save=True)
	# # 	createRealModel(year, region="Kansai", depth=60, withMag=False, save=True)
	# 	year+=1
		
	# #exec models
	year=2000
	while(year<2011):
		# regions = ('Tohoku' ,'EastJapan', 'Kansai', 'Kanto')
		region = 'EastJapan'
		depths = (25, 60, 100)
		# for region in regions:
		for depth in depths:
		# depth = 60
			print(depth, year, region)
			execEtasGaModelClusteredII(year, region, depth=depth, save=True)
			# execGaModel(year, region, depth=depth, save=True)
			# execEtasGaModel(year, region, depth=depth, save=True)	
			execGaModelClusteredII(year, region, depth=depth, save=True)
		
		year+=1

if __name__ == "__main__":
	main()
