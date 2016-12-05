#!/usr/bin/env python3
import random
import models.mathUtil as mathUtil
import earthquake.catalog as catalog
import models.model as model
import gaModel.gaModel_Yuri as ga
import gaModel.GAModelP_AVR as gaModelP_AVR
import gaModel.gaModelWeights as gaModelWeights
import gaModel.gaModel_YuriWithMag as gaWithMag
import gaModel.etasGaModelNP as etasGaModelNP
import models.modelEtasGa as etasGa
import models.randomModel as randomModel
import gaModel.parallelGA as parallelGA
import gaModel.parallelList as parallelList
import time
import numpy as np


def execParallelGARandomParSC(year, region, depth, qntYears=5, times=10, save=True):
	
	observations=list()
	means = list()

	for i in range(qntYears):
		observation=model.loadModelFromFile('../Zona3/sc/3.0'+region+'real'+str(depth)+"_"+str(year+i)+'.txt')
		observation.bins=observation.bins.tolist()
		observations.append(observation)
		means.append(observation.bins)
	mean = np.mean(means)

	for i in range(times):
		CXPB = random.random()
		MUTPB = 1 - CXPB
		start = time.clock()
		modelo=parallelGA.gaModel(100,500,CXPB,MUTPB,observations, year+qntYears, region, mean)
		end = time.clock()
		modelo.mag=True
		if save==True:
			etasGa.saveModelToFile(modelo, 'sc-parallel-random/'+region+'_'+str(depth)+"_"+str(year+qntYears)+str(i)+'.txt')
			
		with open('time_exec/sc-parallel-random'+region+'_'+str(depth)+"_"+str(year+qntYears)+'.txt', "a") as myfile:
			myfile.write(str(end-start))
			myfile.write("\n")

def execParallelListGARandomParSC(year, region, depth, qntYears=5, times=10, save=True):
	
	observations=list()
	means = list()

	for i in range(qntYears):
		observation=model.loadModelFromFile('../Zona3/sc/3.0'+region+'real'+str(depth)+"_"+str(year+i)+'.txt')
		observation.bins=observation.bins.tolist()
		observations.append(observation)
		means.append(observation.bins)
	mean = np.mean(means)

	for i in range(times):
		CXPB = random.random()
		MUTPB = 1 - CXPB
		start = time.clock()
		modelo=parallelList.gaModel(100,500,CXPB,MUTPB,observations, year+qntYears, region, mean)
		end = time.clock()
		modelo.mag=True
		if save==True:
			start = time.clock()
			etasGa.saveModelToFile(modelo, 'sc-parallelList-random/'+region+'_'+str(depth)+"_"+str(year+qntYears)+str(i)+'.txt')
			
		with open('time_exec/sc-parallelList-random'+region+'_'+str(depth)+"_"+str(year+qntYears)+'.txt', "a") as myfile:
			myfile.write(str(end-start))
			myfile.write("\n")

def execParallelListGARandomPar(year, region, depth, qntYears=5, times=10, save=True):
	
	observations=list()
	means = list()

	for i in range(qntYears):
		observation=model.loadModelFromFile('../Zona3/sc/3.0'+region+'real'+str(depth)+"_"+str(year+i)+'.txt')
		observation.bins=observation.bins.tolist()
		observations.append(observation)
		means.append(observation.bins)
	mean = np.mean(means)

	for i in range(times):
		CXPB = random.random()
		MUTPB = 1 - CXPB
		start = time.clock()
		modelo=parallelList.gaModel(100,500,CXPB,MUTPB,observations, year+qntYears, region, mean)
		end = time.clock()
		modelo.mag=True
		if save==True:
			start = time.clock()
			etasGa.saveModelToFile(modelo, 'parallelList-random/'+region+'_'+str(depth)+"_"+str(year+qntYears)+str(i)+'.txt')

		with open('time_exec/parallelList-random'+region+'_'+str(depth)+"_"+str(year+qntYears)+'.txt', "a") as myfile:
			myfile.write(str(end-start))
			myfile.write("\n")

def execParallelGARandomPar(year, region, depth, qntYears=5, times=10, save=True):
	
	observations=list()
	means = list()

	for i in range(qntYears):
		observation=model.loadModelFromFile('../Zona3/sc/3.0'+region+'real'+str(depth)+"_"+str(year+i)+'.txt')
		observation.bins=observation.bins.tolist()
		observations.append(observation)
		means.append(observation.bins)
	mean = np.mean(means)

	for i in range(times):
		CXPB = random.random()
		MUTPB = 1 - CXPB
		start = time.clock()
		modelo=parallelGA.gaModel(100,500,CXPB,MUTPB,observations, year+qntYears, region, mean)
		end = time.clock()
		modelo.mag=True
		if save==True:
			etasGa.saveModelToFile(modelo, 'parallel-random/'+region+'_'+str(depth)+"_"+str(year+qntYears)+str(i)+'.txt')
			
		with open('time_exec/parallel-random'+region+'_'+str(depth)+"_"+str(year+qntYears)+'.txt', "a") as myfile:
			myfile.write(str(end-start))
			myfile.write("\n")

def execParallelGA(year, region, depth, qntYears=5, times=10, save=True):
	
	observations=list()
	means = list()

	for i in range(qntYears):
		observation=model.loadModelFromFile('../Zona3/sc/3.0'+region+'real'+str(depth)+"_"+str(year+i)+'.txt')
		observation.bins=observation.bins.tolist()
		observations.append(observation)
		means.append(observation.bins)
	mean = np.mean(means)

	for i in range(times):
		modelo=parallelGA.gaModel(100,500,0.9,0.1,observations, year+qntYears, region, mean)
		modelo.mag=True
		if save==True:
			etasGa.saveModelToFile(modelo, 'parallel-fixcxmt/'+region+'_'+str(depth)+"_"+str(year+qntYears)+str(i)+'.txt')

def execParallelListGA(year, region, depth, qntYears=5, times=10, save=True):
	
	observations=list()
	means = list()

	for i in range(qntYears):
		observation=model.loadModelFromFile('../Zona3/sc/3.0'+region+'real'+str(depth)+"_"+str(year+i)+'.txt')
		observation.bins=observation.bins.tolist()
		observations.append(observation)
		means.append(observation.bins)
	mean = np.mean(means)

	for i in range(times):
		modelo=parallelList.gaModel(100,500,0.9,0.1,observations, year+qntYears, region, mean)
		modelo.mag=True
		if save==True:
			etasGa.saveModelToFile(modelo, 'parallelList-fixcxmt/'+region+'_'+str(depth)+"_"+str(year+qntYears)+str(i)+'.txt')



def execEtasGaModel(year, region, depth, qntYears=5, times=10, save=True):
	
	observations=list()
	means = list()

	for i in range(qntYears):
		observation=model.loadModelFromFile('../Zona3/sc/3.0'+region+'real'+str(depth)+"_"+str(year+i)+'.txt')
		observation.bins=observation.bins.tolist()
		observations.append(observation)
		means.append(observation.bins)
	mean = np.mean(means)

	for i in range(times):
		modelo=etasGaModelNP.gaModel('non-clustered', 100,0.9,0.1,observations, year+qntYears, region, mean)
		modelo.mag=True
		if save==True:
			etasGa.saveModelToFile(modelo, '../Zona2/listaGA_New/'+region+'_'+str(depth)+"_"+str(year+qntYears)+str(i)+'.txt')

def execGaModel(year, region,  depth, qntYears=5, times=10, save=True):

    observations=list()
    means = list()

    for i in range(qntYears):
    	observation=model.loadModelFromFile('../Zona3/sc/3.0'+region+'real'+str(depth)+"_"+str(year+i)+'.txt')
    	observation.bins=observation.bins.tolist()
    	observations.append(observation)
    	means.append(observation.bins)
    mean = np.mean(means)

    for i in range(times):
    	modelo=ga.gaModel('non-clustered', 100,0.9,0.1,observations,year+qntYears,region, mean)
    	if save==True:
    		model.saveModelToFile(modelo, '../Zona3/gaModel/'+region+'_'+str(depth)+"_"+str(year+qntYears)+str(i)+'.txt')

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
	if depth == 0:
		definicao=model.loadModelDefinition('../params/'+region+'.txt')
	else:
		definicao=model.loadModelDefinition('../params/'+region+'Etas_'+str(depth)+'.txt')
	catalogo=catalog.readFromFile('../data/jmacat_2000_2013.dat')
	catalogo=catalog.filter(catalogo,definicao)
	observacao=model.newModel(definicao, mag=withMag)
	observacao=model.addFromCatalog(observacao,catalogo,year)

	if save==True:
		if observacao.mag==False:
			if depth == 0:
				model.saveModelToFile(observacao, '../Zona2/realData/'+region+'real'+"_"+str(year)+'.txt', real=True)
			else:
				model.saveModelToFile(observacao, '../Zona2/realData/'+str(depth)+region+'real'+str(depth)+"_"+str(year)+'.txt', real=True)
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
	observacao=model.addFromCatalog(observacao,catalogo,year)

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

def createRealModelSC(year, region, depth, withMag=True, save=False):		
	definicao=model.loadModelDefinition('../params/'+region+'Etas_'+str(depth)+'.txt')
	catalogo=catalog.readFromFile('../data/SC-catalog.dat')
	catalogo=catalog.filter(catalogo,definicao)
	observacao=model.newModel(definicao, mag=False)
	observacao=model.addFromCatalog(observacao,catalogo,year)

	if save==True:
		if observacao.mag==False:
			model.saveModelToFile(observacao, '../Zona3/sc-weights/'+str(3.0)+region+'real'+str(depth)+"_"+str(year)+'.txt', real=True)


def createandExecRealModelSCwithP_AVR(year, region, qntYears=5, depth=100, withMag=True, save=True):		
	observations=list()
	means = list()
	for i in range(qntYears):
		definicao=model.loadModelDefinition('../params/'+region+'Etas_'+str(depth)+'.txt')
		catalogo=catalog.readFromFile('../data/SC-catalog.dat')
		catalogo=catalog.filter(catalogo,definicao)
		observacao=model.newModel(definicao, mag=False)
		riskMap=catalog.readFromFileP_AVR('../data/P_AVR-MAP_T30-TTL_TTL_TTL_TOTAL_I45_PS.csv')
		riskMap=catalog.filterP_AVR(riskMap,definicao)

		observacao=model.addFromCatalogP_AVR(observacao, catalogo, riskMap, year)
		observacao.bins = observacao.bins.tolist()
		observations.append(observacao)
		means.append(observacao.bins)
	mean = np.mean(means)

	times = 10
	for i in range(times):
		modelo=gaModelP_AVR.gaModel(10,50,0.9,0.1,observations,year+qntYears, region, mean = mean)
		exit()
		if save==True:
			model.saveModelToFile(modelo, '../Zona3/sc-weights/gamodelPSHM'+region+'_'+str(depth)+"_"+str(year+qntYears)+str(i)+'.txt')

	observations=list()
	means = list()
	for i in range(qntYears):
		definicao=model.loadModelDefinition('../params/'+region+'Etas_'+str(depth)+'.txt')
		catalogo=catalog.readFromFile('../data/SC-catalog.dat')
		catalogo=catalog.filter(catalogo,definicao)
		observacao=model.newModel(definicao, mag=False)
		riskMap=catalog.readFromFileP_AVR('../data/Z_JAPAN-AMP-VS400.csv')
		riskMap=catalog.filterP_AVR(riskMap,definicao)

		observacao=model.addFromCatalogP_AVR(observacao, catalogo, riskMap, year)
		observacao.bins = observacao.bins.tolist()
		observations.append(observacao)
		means.append(observacao.bins)
	mean = np.mean(means)
	
	times = 10
	for i in range(times):
		modelo=gaModelP_AVR.gaModel(100,500,0.9,0.1,observations,year+qntYears,region, mean = mean)
		if save==True:
			model.saveModelToFile(modelo, '../Zona3/sc-weights/gamodel'+'AF'+region+'_'+str(depth)+"_"+str(year+qntYears)+str(i)+'.txt')

def execGaModelSC(year, region,  depth, qntYears=5, times=10, save=True):

    observations=list()
    
    for i in range(qntYears):
        observation=model.loadModelFromFile('../Zona3/sc/3.0'+region+'real'+str(depth)+"_"+str(year+i)+'.txt')
        observation.bins=observation.bins.tolist()
        observations.append(observation)

    for i in range(times):
        modelo=ga.gaModel('sc', 100,0.9,0.1,observations,year+qntYears,region, depth)
        if save==True:
            model.saveModelToFile(modelo, '../Zona3/scModel/gamodel'+region+'_'+str(depth)+"_"+str(year+qntYears)+str(i)+'.txt')

def execEtasGaModelSC(year, region, depth, qntYears=5, times=10, save=True):
	
	observations=list()

	for i in range(qntYears):
		observation=model.loadModelFromFile('../Zona3/sc/3.0'+region+'real'+str(depth)+"_"+str(year+i)+'.txt')
		observation.bins=observation.bins.tolist()
		observations.append(observation)

	for i in range(times):
		modelo=etasGaModelNP.gaModel('sc', 100,0.9,0.1,observations, year+qntYears, region, depth)
		modelo.mag=True
		if save==True:
			model.saveModelToFile(modelo, '../Zona3/scModel/listgamodel'+region+'_'+str(depth)+"_"+str(year+qntYears)+str(i)+'.txt')



def main():
	region = 'Kanto'
	year=2000
	depth = 100
	while(year<=2005):
		print(year, region)
		createandExecRealModelSCwithP_AVR(year, region, save = True)
		year+=1

	region = 'EastJapan'
	year=2000
	depth = 100
	while(year<=2005):
		print(year, region)
		createandExecRealModelSCwithP_AVR(year, region, save = True)
		year+=1

	region = 'Tohoku'
	year=2003
	depth = 100
	while(year<=2005):
		print(year, region)
		createandExecRealModelSCwithP_AVR(year, region, save = True)
		year+=1

	region = 'Kansai'
	year=2000
	depth = 100
	while(year<=2005):
		print(year, region)
		createandExecRealModelSCwithP_AVR(year, region, save = True)
		year+=1


if __name__ == "__main__":
	main()
