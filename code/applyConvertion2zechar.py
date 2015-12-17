import models.modelEtasGa as etasGA
import models.model as model

def applyConvertion2zechar(year=2005,qntYears=5) :
	for n_qntYears in range(qntYears):
		m=etasGA.loadModelFromFile("../Zona/model/teste_etasNP"+str(year+n_qntYears)+"exec.txt")
		m=etasGA.limitTo12(m)

		etasGA.modelToZecharTests(model=m, filename="../Zona/modelTestInZechar/teste_etasNP"+str(year+n_qntYears)+".xml",
		 startDate=str(year+n_qntYears), endDate=str(year+n_qntYears+1))
		
		
		r=etasGA.loadModelFromFile("../Zona/realEtas"+str(year+n_qntYears)+".txt")
		r=etasGA.limitTo12(m)
		
		etasGA.modelToZecharTests(model=r, filename="../Zona/modelTestInZechar/teste_real"+str(year+n_qntYears)+".xml",
		 startDate=str(year+n_qntYears), endDate=str(year+n_qntYears+1))
		
		g=model.loadModelFromFile('../Zona/model/teste_modelo'+str(year+n_qntYears)+'exec.txt')
		g.definitions=r.definitions
		g.definitions[2]['min']=0.0
		g=etasGA.limitTo12(m)
		etasGA.modelToZecharTests(model=g, filename="../Zona/modelTestInZechar/teste_gaModel"+str(year+n_qntYears)+".xml",
		 startDate=str(year+n_qntYears), endDate=str(year+n_qntYears+1))

def applyConvertionWithRI(year=2005, qntYears=5):
	for n_qntYears in range(qntYears):
		m=etasGA.loadModelFromFile("../Zona/model/teste_etasNP"+str(year+n_qntYears)+"exec.txt")
		etasGA.ideaRIinMmodels(m)

		model.saveModelToFile(m, '../Zona/model/teste_etasNP'+str(year+n_qntYears)+"WithRI.txt")

		etasGA.modelToZecharTests(model=m, filename="../Zona/modelTestInZechar/teste_etasNP+ri"+str(year+n_qntYears)+".xml",
		 startDate=str(year+n_qntYears), endDate=str(year+n_qntYears+1))
		
		r=etasGA.loadModelFromFile("../Zona/realEtas"+str(year+n_qntYears)+".txt")
		g=model.loadModelFromFile('../Zona/model/teste_modelo'+str(year+n_qntYears)+'exec.txt')
		g.definitions=r.definitions
		g.definitions[2]['min']=0.0
		etasGA.ideaRIinMmodels(g)
		model.saveModelToFile(g, '../Zona/model/teste_gaModel'+str(year+n_qntYears)+"WithRI.txt")

		etasGA.modelToZecharTests(model=g, filename="../Zona/modelTestInZechar/teste_gaModel+ri"+str(year+n_qntYears)+".xml",
		 startDate=str(year+n_qntYears), endDate=str(year+n_qntYears+1))
