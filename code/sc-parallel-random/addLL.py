import sys
sys.path.append('../')
import models.modelEtasGa as etasGa
import models.model as model
import csep.loglikelihood

def addLoglike2(region, depth, year_begin, year_end):

	year=year_begin
	while(year<=year_end):
		for i in range(10):

			modelL=etasGa.loadModelFromFile(region+'_'+str(depth)+'_'+str(year)+str(i)+'.txt')
			modelL = etasGa.limitTo12(modelL)
			modelO=model.loadModelFromFile('../../Zona2/realData/'+region+'real_'+str(year)+'.txt')
			loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
			modelL.loglikelihood=loglikeValue
			modelL.mag=True
			etasGa.saveModelToFile(modelL,region+'_'+str(depth)+'_'+str(year)+str(i)+'.txt')
			
			with open('loglikelihood'+region+'_'+str(depth)+'_'+str(year)+'.txt', "a") as myfile:
					myfile.write(str(loglikeValue))
					myfile.write("\n")
			print(year, depth, region,i, loglikeValue)
		year+=1

def main():
	regions = ('EastJapan', 'Kanto', 'Kansai', 'Tohoku')
	depth = 100
	for region in regions:
		#the year here already is the target year
		addLoglike2(region, depth, 2005, 2010)



if __name__ == "__main__":
	main()