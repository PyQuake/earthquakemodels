from models.mathUtil import invertPoisson
from math import isinf, exp

#forecast := possible model -> modelLamba
#observation := number of earthquake in which bin, catalog:=modeloOmega
#reference := prob values in from catalog
#nao sao probabilidades, entao preciso arrumar!
#Arrumando o catalog, o do modeloGerado como farei?
def gain(modelLambda, modelOmega, reference):
    gain=0

    if reference==[]:
        probLambda, probOmega = [], []
        probLambda, probOmega = convertToProb(modelLambda, modelOmega)
        if len(probLambda) == len(probOmega):
            for i in range(len(probLambda)):
                p=probLambda[i]
                y=0
                if modelOmega.bins[i]>0:
                    y=1
                p0=probOmega[i]
                if p0>0 and p>0:
                    #TODO: Think if this way is a good way of doing it
                    if p0==1.0:
                        p0=0.9999999999999999
                    gain+=y*(p*(1-p0)/p0-(1-p))+(1-y)*(-p+(1-p)*(p0)/(1-p0))

            return gain
        else:
            raise NameError("Tried to calculate log likelihood for models with different sizes")
    else:
        #TODO: Is there need to use another model as reference?
        raise NameError("gambling Score test with another model as reference is in deveopment...")

def convertToProb(modelLambda, modelOmega):

    probLambda=[]
    probOmega=[]
    for i in range(len(modelLambda.bins)):
        probLambda.append(1-exp(-modelLambda.bins[i]))
        probOmega.append(1-exp(-modelOmega.bins[i]))
    return probLambda, probOmega

def calcGamblingScore(modelLambda, modelOmega, reference=[]):
    gainForecast=gain(modelLambda, modelOmega, reference)
    
    return gainForecast



