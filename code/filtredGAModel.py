#!/usr/bin/env python3
import models.mathUtil as mathUtil
import earthquake.catalog as catalog
import models.model as model
import gaModel.gaModel_Yuri as ga
import models.modelEtasGa as etasGa

def createRealModelClustered(year, region, depth, withMag=True, save=False):		
	definicao=model.loadModelDefinition('../params/'+region+'Etas_'+str(depth)+'.txt')
	catalogo=catalog.readFromFile('../data/clustered_quakes-M.dat')
	catalogo=catalog.filter(catalogo,definicao)
	observacao=model.newModel(definicao, mag=withMag)
	observacao=model.addFromCatalog(observacao,catalogo,year)

	if save==True:
		if observacao.mag==False:
			model.saveModelToFile(observacao, '../Zona3/clustered_listaGA_new_real/'+str(4.0)+region+'real'+str(depth)+"_"+str(year)+'.txt', real=True)


def execGaModelClustered(year, region,  depth, qntYears=5, times=20, save=True):

    observations=list()
    
    for i in range(qntYears):
        observation=model.loadModelFromFile('../Zona3/clustered_listaGA_new_real/'+str(4.0)+region+'real'+str(depth)+"_"+str(year)+'.txt')
        observation.bins=observation.bins.tolist()
        observations.append(observation)

    for i in range(times):
        modelo=ga.gaModel('clustered', 100,0.9,0.1,observations,year+qntYears,region, depth)
        if save==True:
            model.saveModelToFile(modelo, '../Zona3/clustered_gamodel/4.0'+region+'_'+str(depth)+"_"+str(year+qntYears)+str(i+10)+'.txt')

def main():
	depth=25
	year=2000
	region = 'Kanto'
	while(year<2011):
		# regions = ('Tohoku' ,'EastJapan', 'Kansai', 'Kanto')
		# for region in regions:
			# print(region, year, depth)
		# createRealModelClustered(year, region=region, depth=25, withMag=False, save=True)
		execGaModelClustered(year, region, depth=depth, save=True)
		
		year+=1

if __name__ == "__main__":
	main()
