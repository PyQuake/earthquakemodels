import numpy as np

#logbook_gaModelClustered/Tohoku_2011_logbook
#logbook_listaGA_newClustered/EastJapan_2005_logbook
def converter2means(region, year, type):
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

def converter2leastBestClustered(region, year, type):
	year=str(year)
	filename =  "../Zona2/logbook_"+type+"Clustered/"+region+"_"+year+"_logbook.txt"
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

	
	filename =  "../Zona2/dataForR/"+region+"_"+year+"_LastGen25"+type+"Clustered.txt"
	with open(filename, 'w') as f:
		for i in range(10):
			f.write(str(data25[99+100*i]))
			f.write("\n")

	filename =  "../Zona2/dataForR/"+region+"_"+year+"_LastGen60"+type+"Clustered.txt"
	with open(filename, 'w') as f:
		for i in range(10):
			f.write(str(data60[99+100*i]))
			f.write("\n")

	filename =  "../Zona2/dataForR/"+region+"_"+year+"_LastGen100"+type+"Clustered.txt"
	with open(filename, 'w') as f:
		for i in range(10):
			f.write(str(data100[99+100*i]))
			f.write("\n")

	  
def converter2leastBest(type, region, depth, year_begin, year_end):
	
	year=year_begin
	while(year<=year_end):
		print(year)
		data = list()
		for i in range(10):
			filename =  "../Zona2/"+type+'/'+region+"_"+str(depth)+"_"+str(year)+str(i)+".txtloglikelihood.txt"
			f = open(filename, "r")
			for line in f:
				info = line.split()
				data.append(float(info[0]))
			f.close()

		
		filename =  "../Zona2/dataForR/"+type+"_"+region+"_"+str(depth)+"_"+str(year)+".txt"
		with open(filename, 'w') as f:
			for i in range(10):
				f.write(str(data[i]))
				f.write("\n")	
		year+=1

def converter2leastBestHybrid(type, region, depth, year_begin, year_end):
	
	year=year_begin
	while(year<=year_end):
		print(year)
		data = list()
		for i in range(10):
			filename =  "../Zona2/"+type+'/'+type+region+"_"+str(depth)+"_"+str(year)+'_'+str(i)+".txtloglikelihood.txt"
			f = open(filename, "r")
			for line in f:
				info = line.split()
				data.append(float(info[0]))
			f.close()

		
		filename =  "../Zona2/dataForR/"+type+"_"+region+"_"+str(depth)+"_"+str(year)+".txt"
		with open(filename, 'w') as f:
			for i in range(10):
				f.write(str(data[i]))
				f.write("\n")
		year+=1


def main():
	types = ('listaGA_New', 'gaModel', 'clustered_listaGA_new', 'clustered_gaModel')
	regions = ('EastJapan', 'Kansai', 'Kanto', 'Tohoku')
	depths = (25, 60, 100)
	
	for region in regions:
		print(region)
		for depth in depths:
			print(depth)
			converter2leastBestHybrid('hybrid_gaModel', region, depth, 2005, 2010)
			converter2leastBestHybrid('hybrid_ListaGA_New', region, depth, 2005, 2010)
			for t in types:
				print(t)
				converter2leastBest(t, region, depth, 2005, 2010)

	

if __name__ == "__main__":
	main()
