
#!/usr/bin/env python3
import models.mathUtil as mathUtil
import earthquake.catalog as catalog
import models.model as model
import gaModel.gaModel_Yuri as ga
import gaModel.etasGaModelNP as etasGaModelNP
import models.modelEtasGa as etasGa

def createRealModelClustered(year, region, depth, withMag=True, save=False):		
	definicao=model.loadModelDefinition('../params/'+region+'Etas_'+str(depth)+'.txt')
	catalogo=catalog.readFromFile('../data/clustered_quakes-M.dat')
	catalogo=catalog.filter(catalogo,definicao)
	observacao=model.newModel(definicao, mag=withMag)
	observacao=model.addFromCatalog(observacao,catalogo,year)

	if save==True:
		if observacao.mag==False:
			model.saveModelToFile(observacao, '../Zona3/clustered_gaModel_real/'+str(4.0)+region+'real'+str(depth)+"_"+str(year)+'.txt', real=True)

def execEtasGaModelClustered(year, region, depth, qntYears=5, times=30, save=True):
	
	observations=list()

	for i in range(qntYears):
		observation=model.loadModelFromFile('../Zona3/clustered_gaModel_real/'+str(4.0)+region+'real'+str(depth)+"_"+str(year)+'.txt', real=True)
		observation.bins=observation.bins.tolist()
		observations.append(observation)

	for i in range(times):
		modelo=etasGaModelNP.gaModel('clustered',100,0.9,0.1,observations, year+qntYears, region, depth)
		modelo.mag=True
		if save==True:
			etasGa.saveModelToFile(modelo, '../Zona2/clustered_listaGA_new/4.0'+region+'_'+str(depth)+"_"+str(year+qntYears)+str(i)+'.txt')

def main():
	depth=25
	year=2000
	while(year<2010):
		regions = ('Tohoku' ,'EastJapan', 'Kansai', 'Kanto')
		# createRealModelClustered(year, region=region, depth=25, withMag=False, save=True)
		execEtasGaModelClustered(year, region, depth=depth, save=True)
		
		year+=1

if __name__ == "__main__":
	main()
