import numpy as np
import re

def converter(region, year, type):
	year=str(year)
	filename =  "../Zona2/logbook_"+type+"/"+region+"_"+year+"_logbook.txt"
	f = open(filename, "r")

	data25=list()
	data60=list()#1010
	data100=list()#2020

	for line in f:
		info = line.split()
		if info[4] != 'max':
			if len(data25) < 1000:
				data25.append(float(info[4]))
			elif len(data60) < 1000:
				data60.append(float(info[4]))
			else:
				data100.append(float(info[4]))
	f.close()

	std25 = list()
	media25 = list()
	for i in range(100):#i e a geracao
		aux = [0] * 10
		for j in range(10):#j e a repeticao
			aux[j] = data25[i+(j*100)]
		std25.append(np.std(aux))
		media25.append(np.mean(aux))
	filename =  "../Zona2/dataForR/"+region+"_"+year+"_Media25"+type+".txt"
	with open(filename, 'w') as f:
		for item in media25:
			f.write(str(item))
			f.write("\n")
	filename =  "../Zona2/dataForR/"+region+"_"+year+"_STD25"+type+".txt"
	with open(filename, 'w') as f:
		for item in std25:
			f.write(str(item))
			f.write("\n")

	std60 = list()
	media60 = list()
	for i in range(100):#i e a geracao
		aux = [0] * 10
		for j in range(10):#j e a repeticao
			aux[j] = data60[i+(j*100)]
		std60.append(np.std(aux))
		media60.append(np.mean(aux))
	filename =  "../Zona2/dataForR/"+region+"_"+year+"_Media60"+type+".txt"
	with open(filename, 'w') as f:
		for item in media60:
			f.write(str(item))
			f.write("\n")
	filename =  "../Zona2/dataForR/"+region+"_"+year+"_STD60"+type+".txt"
	with open(filename, 'w') as f:
		for item in std60:
			f.write(str(item))
			f.write("\n")

	std100 = list()
	media100 = list()
	for i in range(100):#i e a geracao
		aux = [0] * 10
		for j in range(10):#j e a repeticao
			aux[j] = data100[i+(j*100)]
		std100.append(np.std(aux))
		media100.append(np.mean(aux))
	filename =  "../Zona2/dataForR/"+region+"_"+year+"_Media100"+type+".txt"
	with open(filename, 'w') as f:
		for item in media100:
			f.write(str(item))
			f.write("\n")
	filename =  "../Zona2/dataForR/"+region+"_"+year+"_STD100"+type+".txt"
	with open(filename, 'w') as f:
		for item in std100:
			f.write(str(item))
			f.write("\n")
	  
year = 2000
while (year<=2005):
	converter(region='Kanto', year=year, type="gaModel")
	converter(region='Kanto', year=year, type='listaGA_New')
	converter(region='EastJapan', year=year, type="gaModel")
	converter(region='EastJapan', year=year, type='listaGA_New')
	converter(region='Tohoku', year=year, type="gaModel")
	converter(region='Tohoku', year=year, type='listaGA_New')
	converter(region='Kansai', year=year, type="gaModel")
	converter(region='Kansai', year=year, type='listaGA_New')
	year+=1