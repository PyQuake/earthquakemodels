import models.modelEtasGa as etasGa
import models.model as model
import csep.loglikelihood

def addLoglike2(type, region, depth, year_begin, year_end):

	year=year_begin
	while(year<=year_end):
		print(year)
		for i in range(10):
			modelL=etasGa.loadModelFromFile('../Zona2/'+type+'/'+region+'_'+str(depth)+'_'+str(year)+str(i)+'.txt')
			modelL = etasGa.limitTo12(modelL)
			modelO=model.loadModelFromFile('../Zona2/realData/'+region+'real'+"_"+str(year)+'.txt')
			loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
			modelL.loglikelihood=0
			modelL.mag=True
			etasGa.saveModelToFile(modelL,'../Zona2/'+type+'/'+region+'_'+str(depth)+'_'+str(year)+str(i)+'.txt')
			
			with open('../Zona2/'+type+'/'+region+'_'+str(depth)+'_'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
					myfile.write(str(loglikeValue))
					myfile.write("\n")
		year+=1

def addLoglike2SC(type, region, depth, year_begin, year_end):

	year=year_begin
	while(year<=year_end):
		print(year)
		for i in range(10):
			if type == 'gaModel':
				modelL=etasGa.loadModelFromFile('../Zona3/scModel/gamodel'+region+'_'+str(depth)+'_'+str(year)+str(i)+'.txt')	
			else:
				modelL=etasGa.loadModelFromFile('../Zona3/scModel/eastgamodel'+region+'_'+str(depth)+'_'+str(year)+str(i)+'.txt')	
			modelL = etasGa.limitTo12(modelL)
			modelO=model.loadModelFromFile('../Zona2/realData/'+region+'real'+"_"+str(year)+'.txt')
			loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
			modelL.loglikelihood=0
			modelL.mag=True
			etasGa.saveModelToFile(modelL,'../Zona3/'+type+'/SC'+region+'_'+str(depth)+'_'+str(year)+str(i)+'.txt')
			#"../Zona2/"+type+'/hybrid_'+file[1]+'_'+file[2]+region+"_"+str(depth)+"_"+str(year)+'_'+str(i)+".txtloglikelihood.txt"
			#'../Zona3/sc/3.0'+region+'real'+str(depth)+"_"+str(year+i)+'.txt')	
			
			with open('../Zona3/'+type+'/SC'+region+'_'+str(depth)+'_'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
					myfile.write(str(loglikeValue))
					myfile.write("\n")
		year+=1


def main():
	types = ('gaModel', 'listaGA_new')
	regions = ('EastJapan', 'Kanto')
	depth = 100
	for t in types:
		print(t)
		for region in regions:
			print(region)
			#the year here already is the target year
			addLoglike2SC(t, region, depth, 2005, 2010)



if __name__ == "__main__":
	main()