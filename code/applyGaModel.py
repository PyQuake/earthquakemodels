#!/usr/bin/env python

import earthquake.catalog as catalog
import models.model as model
import gaModel.gaModel_Yuri as ga
import gaModel.gaModel_YuriWithMag as gaWithMag

def execGaModel(year, times):
	observacao=model.loadModelFromFile('../Zona/real'+str(year)+'.txt',False)
	definicao=model.loadModelDefinition('../params/Kanto.txt')
	modelo=model.newModel(definicao, False)
	modelo=ga.gaModel(100,0.9,0.1,observacao)
	model.saveModelToFile(modelo, '../Zona/model/modelo'+str(year)+'.txt')
	for i in range(times):
		modelo=ga.gaModel(100,0.9,0.1,modelo)
		model.saveModelToFile(modelo, '../Zona/model/modeloWithMag'+str(year)+"exec"+str(i)+'.txt')

def execGaModelWithMag(year, times):
	observacao=model.loadModelFromFile('../Zona/realWithMag'+str(year)+'.txt')
	definicao=model.loadModelDefinition('../params/KantoWithMag.txt')
	modelo=model.newModel(definicao)
	auxModelo=model.convert2DToArray(modelo, modelo.definitions)
	auxModelo.bins=auxModelo.bins.tolist()
	for i in range(times):
		modelo=ga.gaModel(100,0.9,0.1,auxModelo)
		model.saveModelToFile(model.convertArrayto2D(modelo,definicao), '../Zona/model/modeloWithMag'+str(year)+"exec"+str(i)+'.txt')


def createRealModel(year, withMag=True):
	definicao=model.loadModelDefinition('../params/KantoWithMag.txt')
	catalogo=catalog.readFromFile('../data/jmacat_2000_2013.dat')
	catalogo=catalog.filter(catalogo,definicao)
	observacao=model.newModel(definicao, mag=True)
	observacao=model.addFromCatalog(observacao,catalogo,year)
	
	if observacao.mag==False:
		model.saveModelToFile(observacao, '../Zona/real'+str(year)+'.txt')
	else:
		model.saveModelToFile(observacao, '../Zona/realWithMag'+str(year)+'.txt')
	

	if __name__ == "__main__":
	    execGaModelWithMag()