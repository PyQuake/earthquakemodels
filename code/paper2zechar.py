import models.model as model
import models.modelEtasGa as etasGa
import numpy as np

region="Kanto"
year=2006
while(year<=2010):
	a=model.loadModelFromFile("../Zona/paper_exp/MediaNP"+region+'_'+str(year)+"cleaned.txt")
	etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaNP"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
	a=model.loadModelFromFile("../Zona/paper_exp/MediaModelo"+region+'_'+str(year)+"cleaned.txt")
	etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaModelo"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
	print(sum(a.bins),year, region)
	year+=1

region="Kansai"
year=2006
while(year<=2010):
	a=model.loadModelFromFile("../Zona/paper_exp/MediaNP"+region+'_'+str(year)+"cleaned.txt")
	print(sum(a.bins),year,region)
	etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaNP"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
	a=model.loadModelFromFile("../Zona/paper_exp/MediaModelo"+region+'_'+str(year)+"cleaned.txt")
	etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaModelo"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
	print(sum(a.bins),year, region)
	year+=1

region="EastJapan"
year=2006
while(year<=2010):
	a=model.loadModelFromFile("../Zona/paper_exp/MediaNP"+region+'_'+str(year)+"cleaned.txt")
	print(sum(a.bins),year,region)
	etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaNP"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
	a=model.loadModelFromFile("../Zona/paper_exp/MediaModelo"+region+'_'+str(year)+"cleaned.txt")
	etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaModelo"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
	print(sum(a.bins),year, region)
	year+=1

region="Tohoku"
year=2006
while(year<=2010):
	a=model.loadModelFromFile("../Zona/paper_exp/MediaNP"+region+'_'+str(year)+"cleaned.txt")
	print(sum(a.bins),year,region)
	etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaNP"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
	a=model.loadModelFromFile("../Zona/paper_exp/MediaModelo"+region+'_'+str(year)+"cleaned.txt")
	etasGa.modelToZecharTests(a, "../zechar_sw/gaModels"+str(year)+"/"+region+"MediaModelo"+str(year)+".xml", str(00)+str(00)+str(year), str(00)+str(00)+str(year+1))
	print(sum(a.bins),year, region)
	year+=1