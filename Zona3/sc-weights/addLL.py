import sys
sys.path.append('../../code')
import models.modelEtasGa as etasGa
import models.model as model
import csep.loglikelihood

def addLoglike2(region, depth, year_begin, year_end):

	year=year_begin
	while(year<=year_end):
		for i in range(10):

			modelL=etasGa.loadModelFromFile('gamodelPSHM'+region+'_'+str(depth)+'_'+str(year)+str(i)+'.txt')
			modelL = etasGa.limitTo12(modelL)
			modelO=model.loadModelFromFile('../../Zona2/realData/'+region+'real'+"_"+str(year)+'.txt')
			loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
			modelL.loglikelihood=loglikeValue
			modelL.mag=True
			etasGa.saveModelToFile(modelL,'gamodelPSHM'+region+'_'+str(depth)+'_'+str(year)+str(i)+'.txt')
			
			with open('loglikelihoodAF'+region+'_'+str(depth)+'_'+str(year)+'.txt', "a") as myfile:
					myfile.write(str(loglikeValue))
					myfile.write("\n")
			print(year, depth, region,i, loglikeValue)

			modelL=etasGa.loadModelFromFile('gamodelAF'+region+'_'+str(depth)+'_'+str(year)+str(i)+'.txt')
			modelL = etasGa.limitTo12(modelL)
			modelO=model.loadModelFromFile('../../Zona2/realData/'+region+'real'+"_"+str(year)+'.txt')
			loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
			modelL.loglikelihood=loglikeValue
			modelL.mag=True
			etasGa.saveModelToFile(modelL,'gamodelAF'+region+'_'+str(depth)+'_'+str(year)+str(i)+'.txt')
			
			with open('loglikelihoodAF'+region+'_'+str(depth)+'_'+str(year)+'.txt', "a") as myfile:
					myfile.write(str(loglikeValue))
					myfile.write("\n")
			print(year, depth, region,i, loglikeValue)
		year+=1

def main():
	region ='Kanto'
	depth = 100
	#the year here already is the target year
	addLoglike2(region, depth, 2005, 2010)



if __name__ == "__main__":
	main()