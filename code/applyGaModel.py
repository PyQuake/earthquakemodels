import earthquake.catalog as catalog
import models.model as model
import gaModel.gaModel_Yuri as ga

def execGaModel(year):
	definicao=model.loadModelDefinition('../params/Kanto.txt')
	catalogo=catalog.readFromFile('../data/jmacat_2000_2013.dat')
	catalogo=catalog.filter(catalogo,definicao)
	observacao=model.newModel(definicao)
	observacao=model.addFromCatalog(observacao,catalogo,year)
	
	model.saveModelToFile(observacao, '../Zona/real'+str(year)+'.txt')
	

	modelo=model.newModel(definicao)
	modelo=ga.gaModel(100,0.9,0.1,observacao)
	
	model.saveModelToFile(modelo, '../Zona/modelo'+str(year)+'.txt')