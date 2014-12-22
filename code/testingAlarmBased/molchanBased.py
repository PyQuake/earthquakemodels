#TODO: Check the comments
#TODO: Normalizing in areaUnder, why????

import random
import models.mathUtil as mathUtil

#In this case the catalog is the bins/earthquake in the region studied and filtred already
#they sould have the same len

#Arguments are their bins, should it be changed???
def molchan(modelLambda, modelOmega, catalog):

    if(len(modelLambda)==len(modelOmega)==len(catalog)):
    	#TODO: Check how this normalize is done
    	referenceValues=[]
    	referenceValues=mathUtil.normalize(modelOmega)
		#TODO: e so somar os bins do Omega? Uma vez que a gente quer testar o modelo nosso contra os dados reais?
    	N = sum(catalog)
    	#o que o claus tinha comentado aqui?????????
    	#tem tamanho N+1 no zechar, aqui como fica?
    	trajectory=[]


    	#I need to order the in decresing order the values of modelOmega
	    #I also need to have the same positions in the others, so thats what the zip is for
    	fullData=[]
    	for value, lam, cat in zip(referenceValues, modelLambda, catalog):
    		fullData.append((value,lam,cat))
    	fullData.sort()
    	fullData.reverse()

    	#Sera que vale a pena separar um do outro?
    	hits=0
    	for i in range(len(fullData)):
    		tau=fullData[i][0]
    		hitsInThisBin=fullData[i][2]
    		if hitsInThisBin>0:
    			thresholdInThisBin=fullData[i][1]
    			thresholdInNextBin=fullData[min(i+1,len(fullData)-1)][1]
    			while thresholdInThisBin==thresholdInNextBin and i<=len(fullData)-2:
    				i+=1
    				tau+=fullData[i][0]
    				hitsInThisBin+=fullData[i][2]
    				if i<len(fullData)-1:
    					thresholdInNextBin=fullData[i+1][1]
    				else:
    					thresholdInNextBin=float('-Infinity')

    			for j in range(hitsInThisBin):
    				trajectory.insert(hits+j+1,tau)
    			hits+=hitsInThisBin
    			if hits==N:
    				break
    	return trajectory


def areaUnderTrajectory(molchanTrajectory, tau):

    n=0
    i=1

    while(i<len(molchanTrajectory)):
    	if molchanTrajectory[i]<tau:
    		n=i
    	else:
    		n=i-1
    		break
    	i+=1

    N = len(molchanTrajectory)-1
    height=[]

    for i in range(N+1):
    	height.append(N-i/N)

    area=0
    for i in range(n-1):
    	area+=height[i]*(molchanTrajectory[i+1]-molchanTrajectory[i])
    area+=height[n]*(tau - molchanTrajectory[n])

    area /= tau
    return area
    

def assTest(modelLambda, modelOmega, catalog, tauSteps=0.01):
	"""
	Calculates the ASS alarm test function defined by Zechar. 
	Its as alarm based test that considers regions, threshold, miss rate and hits.
	The param should be an model with bins that divides one region, and every bin should contain the quatity of earthquakes
	"""
	molchanTrajectory=molchan(modelLambda, modelOmega, catalog)
	print(len(molchanTrajectory))
	assTrajectory=[]

	limitRange=int(1/tauSteps)
	for i in range(limitRange):
		tau=(i+1)*tauSteps
		ass=1-areaUnderTrajectory(molchanTrajectory, tau)
		assTrajectory.insert(i,ass)

	return assTrajectory
