import models.model as model
import models.modelEtasGa as etasGa

region="Kanto"
year=2006
while(year<=2010):
	a=model.loadModelFromFile("../Zona/paper_exp/MediaNP_Hybrid"+region+'_'+str(year)+"cleaned.txt")
	print(a.bins,year,region)
	etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaNP_Hybrid"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
	a=model.loadModelFromFile("../Zona/paper_exp/MediaModelo_Hybrid"+region+'_'+str(year)+"cleaned.txt")
	etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaModelo_Hybrid"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
	print(sum(a.bins),year, region)
	year+=1

region="Kansai"
year=2006
while(year<=2010):
	a=model.loadModelFromFile("../Zona/paper_exp/MediaNP_Hybrid"+region+'_'+str(year)+"cleaned.txt")
	print(sum(a.bins),year,region)
	etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaNP_Hybrid"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
	a=model.loadModelFromFile("../Zona/paper_exp/MediaModelo_Hybrid"+region+'_'+str(year)+"cleaned.txt")
	etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaModelo_Hybrid"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
	print(sum(a.bins),year, region)
	year+=1

region="EastJapan"
year=2006
while(year<=2010):
	a=model.loadModelFromFile("../Zona/paper_exp/MediaNP_Hybrid"+region+'_'+str(year)+"cleaned.txt")
	print(sum(a.bins),year,region)
	etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaNP_Hybrid"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
	a=model.loadModelFromFile("../Zona/paper_exp/MediaModelo_Hybrid"+region+'_'+str(year)+"cleaned.txt")
	etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaModelo_Hybrid"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
	print(sum(a.bins),year, region)
	year+=1

region="Tohoku"
year=2006
while(year<=2010):
	a=model.loadModelFromFile("../Zona/paper_exp/MediaNP_Hybrid"+region+'_'+str(year)+"cleaned.txt")
	print(sum(a.bins),year,region)
	etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaNP_Hybrid"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
	a=model.loadModelFromFile("../Zona/paper_exp/MediaModelo_Hybrid"+region+'_'+str(year)+"cleaned.txt")
	etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaModelo_Hybrid"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
	print(sum(a.bins),year, region)
	year+=1