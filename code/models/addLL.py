import sys
sys.path.append('../')
import models.modelEtasGa as etasGa
import models.model as model
import csep.loglikelihood

def addLoglike2(filename, region, depth, year, i, loglikelihoodFile):
		
		modelL=etasGa.loadModelFromFile(filename)
		modelL = etasGa.limitTo12(modelL)
		modelO=model.loadModelFromFile('../../Zona2/realData/'+region+'real_'+str(year)+'.txt')
		loglikeValue=csep.loglikelihood.calcLogLikelihood(modelL,modelO)
		modelL.loglikelihood=loglikeValue
		modelL.mag=True
		etasGa.saveModelToFile(modelL,region+'_'+str(depth)+'_'+str(year)+str(i)+'.txt')
		
		with open(loglikelihoodFile, "a") as myfile:
				myfile.write(str(loglikeValue))
				myfile.write("\n")
		print(year, depth, region,i, loglikeValue)
		year+=1

def main():
	region = 'Kanto'
	depth = 100
	qntYears = 5
	# for region in regions:  
	region='Kanto'
	year=2000
	while((year+qntYears)<=2010):
		for i in range(10):
			filename = '../sc-parallelList-random/'+region+'_'+str(depth)+"_"+str(year+qntYears)+str(i)+'.txt'
			loglikelihoodFile = '../loglike/sc-parallelList-random'+region+'_'+str(depth)+"_"+str(year+qntYears)+'.txt'
			#the year here already is the target year
			addLoglike2(filename, region, depth, year, i, loglikelihoodFile)
			
			filename = '../parallelList-random/'+region+'_'+str(depth)+"_"+str(year+qntYears)+str(i)+'.txt'
			loglikelihoodFile = '../loglike/parallelList-random'+region+'_'+str(depth)+"_"+str(year+qntYears)+'.txt'
			#the year here already is the target year
			addLoglike2(filename, region, depth, year, i, loglikelihoodFile)

			filename = '../parallel-random/'+region+'_'+str(depth)+"_"+str(year+qntYears)+str(i)+'.txt'
			loglikelihoodFile = '../loglike/parallel-random'+region+'_'+str(depth)+"_"+str(year+qntYears)+'.txt'
			#the year here already is the target year
			addLoglike2(filename, region, depth, year, i, loglikelihoodFile)

			filename = '../sc-parallel-random/'+region+'_'+str(depth)+"_"+str(year+qntYears)+str(i)+'.txt'
			loglikelihoodFile = '../loglike/sc-parallel-random'+region+'_'+str(depth)+"_"+str(year+qntYears)+'.txt'
			#the year here already is the target year
			addLoglike2(filename, region, depth, year, i, loglikelihoodFile)
		year+=1



if __name__ == "__main__":
	main()


# 'sc-parallelList-random/'+region+'_'+str(depth)+"_"+str(year+qntYears)+str(i)+'.txt')
# 'parallelList-random/'+region+'_'+str(depth)+"_"+str(year+qntYears)+str(i)+'.txt')
# 'parallel-random/'+region+'_'+str(depth)+"_"+str(year+qntYears)+str(i)+'.txt')