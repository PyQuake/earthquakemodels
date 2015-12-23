#!/usr/bin/env python3
import models.mathUtil as mathUtil
import earthquake.catalog as catalog
import models.model as model
import gaModel.gaModel_Yuri as ga
import gaModel.gaModel_YuriWithMag as gaWithMag
import gaModel.etasGaModelNP as etasGaModelNP
import models.modelEtasGa as etasGa
import sys

def execEtasGaModel(year, region, qntYears=5, times=10, save=False):
	
	observations=list()

	for i in range(qntYears):
		observation=etasGa.loadModelFromFile('../Zona/'+region+'real'+str(year+i)+'.txt')
		observation.bins=observation.bins.tolist()
		observations.append(observation)

	# definicao=model.loadModelDefinition('../params/KantoEtas.txt')

	for i in range(times):
		modelo=etasGaModelNP.gaModel(100,0.9,0.1,observations, year)
		modelo.mag=True
		if save==True:
			etasGa.saveModelToFile(modelo, '../Zona/model/'+region+'teste_etasNP'+str(year+qntYears)+str(i)+'.txt')

def execGaModel(year, region, qntYears=5, times=10, save=False):

	observations=list()

	for i in range(qntYears):
		observation=model.loadModelFromFile('../Zona/'+region+'real'+str(year+i)+'.txt')
		observation.bins=observation.bins.tolist()
		observations.append(observation)

	# definicao=model.loadModelDefinition('../params/Kanto.txt')

	for i in range(times):
		modelo=ga.gaModel(100,0.9,0.1,observations,year)
		if save==True:
			model.saveModelToFile(modelo, '../Zona/model/'+region+'teste_modelo'+str(year+qntYears)+str(i)+'.txt')

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


def createRealModel(year, region, withMag=True, save=False):
	# if (withMag==True):
	definicao=model.loadModelDefinition('../params/'+region+'WithMag.txt')
	# else:
	# 	definicao=model.loadModelDefinition('../params/'+region+'.txt')
	catalogo=catalog.readFromFile('../data/jmacat_2000_2013.dat')
	catalogo=catalog.filter(catalogo,definicao)
	observacao=model.newModel(definicao, mag=withMag)
	observacao=model.addFromCatalog(observacao,catalogo,year)
	
	if save==True:
		if observacao.mag==False:
			model.saveModelToFile(observacao, '../Zona/'+region+'real'+str(year)+'.txt')
		else:
			model.saveModelToFile(observacao, '../Zona/'+region+'realWithMag'+str(year)+'.txt')

	return observacao

#Actually, in this case, its kind of a mix between withMag and withoutMag
#Hence, we want info about mag, but we are not incorporating it to the data (maybe this will change)
#we need to adapt from both versions
def createRealModelforEtas(year, region, save=False):
	definition=model.loadModelDefinition('../params/'+region+'Etas.txt')
	catalogo=catalog.readFromFile('../data/jmacat_2000_2013.dat')
	catalogo=catalog.filter(catalogo,definition)
	observation=etasGa.newModel(definition)
	observation=etasGa.addFromCatalog(observation,catalogo,year)
	# observation.prob=mathUtil.normalize(observation.bins)

	observation.mag=True
	if save==True:
		etasGa.saveModelToFile(observation, '../Zona/'+region+'realEtas'+str(year)+'.txt')
	
	return observation

def main():
	print(sys.argv[1])
	year=2000
	while year<2011:
		# print("Kanto", year)
		# region = "Kanto"
		# createRealModelforEtas(year, region, save=True)
		# createRealModel(year, region, withMag=False, save=True)
		# print("Kansai", year)
		# region = "Kansai"
		# # # createRealModelforEtas(year, region, save=True)
		# createRealModel(year, region, withMag=False, save=True)
		print("Tohoku", year)
		region = "Tohoku"
		# # # createRealModelforEtas(year, region, save=True)
		# createRealModel(year, region, withMag=False, save=True)
		# print("EastJapan", year)
		# region = "EastJapan"
		# # # createRealModelforEtas(year, region, save=True)
		# createRealModel(year, region, withMag=False, save=True)
		
		# execGaModel(year, region,save=True)
		#this should not be used
		# execGaModelWithMag(year,10,True)
		execEtasGaModel(year, region, save=True)
		year+=1

if __name__ == "__main__":
	main()
