#TODO: Check the comments
#TODO: Normalizing in areaUnder, why????

import random
import models.mathUtil as mathUtil

#In this case the catalog is the bins/earthquake in the region studied and filtred already
#they sould have the same len

#Arguments are their bins, should it be changed???
def molchan(modelLambda, modelOmega):

    if len(modelLambda.bins)==len(modelOmega.bins):
    	#TODO: Check how this normalize is done
    	referenceValues=[]
    	referenceValues[:]=[x+1 for x in modelOmega.bins]
    	
    	referenceValues=mathUtil.normalize(referenceValues)
		#TODO: e so somar os bins do Omega? Uma vez que a gente quer testar o modelo nosso contra os dados reais?
    	N = sum(modelOmega.bins)
    	#o que o claus tinha comentado aqui?????????
    	#tem tamanho N+1 no zechar, aqui como fica?
    	trajectory=[0]*(N+1)

    	#I need to order the in decresing order the values of modelOmega
	    #I also need to have the same positions in the others, so thats what the zip is for
    	fullData=[]
    	for lam,value in zip(modelLambda.bins, referenceValues):
    		fullData.append((lam, value))
    	fullData.sort()
    	fullData.reverse()

    	testingValues=[]
    	referenceValues=[]
    	for data in fullData:
    		testingValues.append(data[0])
    		referenceValues.append(data[1])

    	hits=0
    	tau=0
    	for i in range(len(modelOmega.bins)):
    		tau+=referenceValues[i]
    		hitsInThisBin=0
    		hitsInThisBin=modelOmega.bins[i]
    		if hitsInThisBin>0:
    			thresholdInThisBin=testingValues[i]
    			thresholdInNextBin=fullData[min(i+1,len(testingValues)-1)]
    			while thresholdInThisBin==thresholdInNextBin and i<=len(testingValues)-2:
    				i+=1
    				tau+=referenceValues[i]
    				hitsInThisBin+=modelOmega.bins[i]
    				if i<(len(testingValues)-1):
    					thresholdInNextBin=testingValues[i+1]
    				else:
    					thresholdInNextBin=float('-Infinity')
    			for j in range(hitsInThisBin):
    				trajectory[hits+j+1]=tau
    			hits+=hitsInThisBin
    			if hits==N:
    				break
    	return trajectory

def whichLegAreWeOn(molchanTrajectory, tau):
	
	n=0
	for i in range(len(molchanTrajectory)):
		if molchanTrajectory[i]<tau:
			n=i
		else:
			return(i-1)
	return n


def areaUnderTrajectory(molchanTrajectory, tau):

    n=whichLegAreWeOn(molchanTrajectory, tau)

    N = len(molchanTrajectory)-1
    height=[]

    for i in range(len(molchanTrajectory)):
    	height.append((N-i)/N)

    area=0
    index=0
    for i in range(n):
        area+=height[index]*(molchanTrajectory[index+1]-molchanTrajectory[index])
        index+=1
    area+=height[n]*(tau-molchanTrajectory[n])
    
    area/=tau
    # print(area)
    return area
    

def assTest(modelLambda, modelOmega, tauSteps=0.01):
    """
    Calculates the ASS alarm test function defined by Zechar. 
    Its as alarm based test that considers regions, threshold, miss rate and hits.
    The param should be an model with bins that divides one region, and every bin should contain the quatity of earthquakes
    """
    molchanTrajectory=molchan(modelLambda, modelOmega)
    assTrajectory=[]

    limitRange=int(1/tauSteps)
    for i in range(limitRange):
        tau=(i+1)*tauSteps
        ass=1-areaUnderTrajectory(molchanTrajectory, tau)
        assTrajectory.append(ass)
    # print(assTrajectory)
    return assTrajectory
