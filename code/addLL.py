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
			modelO=model.loadModelFromFile('../Zona2/realData/3.0'+region+'real'+str(depth)+"_"+str(year)+'.txt')
			loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
			modelL.loglikelihood=0
			modelL.mag=True
			etasGa.saveModelToFile(modelL,'../Zona2/'+type+'/'+region+'_'+str(depth)+'_'+str(year)+str(i)+'.txt')

			print(loglikeValue, i, sum(modelL.bins), sum(modelO.bins))
			with open('../Zona2/'+type+'/'+region+'_'+str(depth)+'_'+str(year)+str(i)+'.txtloglikelihood.txt', "w") as myfile:
					myfile.write(str(loglikeValue))
					myfile.write("\n")
		year+=1

def main():
	types = ('listaGA_New', 'gaModel', 'clustered_listaGA_new', 'clustered_gaModel')
	regions = ('EastJapan', 'Kansai', 'Kanto', 'Tohoku')
	depths = (25, 60, 100)
	for t in types:
		print(t)
		for region in regions:
			print(region)
			for depth in depths:
				print(depth)
		#the year here already is the target year
				addLoglike2(t, region, depth, 2005, 2010)

def mainTESTE():
	t = 'listaGA_New'
	region = 'EastJapan'
	depth = 100
	#the year here already is the target year
	addLoglike2(t, region, depth, 2005, 2010)

if __name__ == "__main__":
	# mainTESTE()
	main()