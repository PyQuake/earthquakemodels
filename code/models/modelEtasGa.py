#import rpy2.robjects as robjects
import datetime
import numpy
from models.mathUtil import invertPoisson
# import numpy
import datetime
import models.mathUtil as mathUtil
import math
import random

class model(object):
    pass

#TODO: is this function relly necessary?
def addFromCatalog(model,catalog, year):
"""
This is a copy of the addFromCatalog from the model.py code
"""
    k, l, index = 0, 0, 0

    # TODO: nao usar key como nome de variavel aqui (criar um dicionario se necessario)
    # TODO: calcular o numero de keys in definition
    range_lon,step_lon,min_lon,max_lon,bins_lon=0,0,0,0,0
    range_lat,step_lat,min_lat,max_lat,bins_lat=0,0,0,0,0
    for definition in model.definitions:
        if definition['key'] == 'lon':
            range_lon = definition['step'] * definition['bins']
            step_lon = definition['step']
            min_lon = definition['min']
            max_lon = definition['min'] + (definition['bins'] * definition['step'])
            bins_lon = definition['bins']
        if definition['key'] == 'lat':
            range_lat = definition['step'] * definition['bins']
            step_lat = definition['step']
            min_lat = definition['min']
            max_lat = definition['min'] + (definition['bins'] * definition['step'])
            bins_lat = definition['bins']
    # TODO: limpar isto um pouco
    for m in range(len(catalog)):
        #kind of a filter, we should define how we are going to filter by year
        if catalog[m]['year'] == year:  
            if catalog[m]['lon']>min_lon and catalog[m]['lon']<max_lon:
                if catalog[m]['lat']>min_lat and catalog[m]['lat']<max_lat:
                        #calculating the adequated bin for a coordinate of a earthquake
                        for i in range(bins_lon):    
                            index = (step_lon*i) + min_lon
                            if catalog[m]['lon']>=index and catalog[m]['lon']<(index+step_lon): 
                                if index+step_lon>max_lon: #to avoid the last index to be out of limits
                                    k -= 1
                                break
                            k += 1
                        for j in range(bins_lat):
                            index = (step_lat*j) + min_lat
                            if catalog[m]['lat']>=index and catalog[m]['lat']<(index+step_lat):
                                if index+step_lat>max_lat: #to avoid the last index to be out of limits
                                    l -= 1
                                break
                            l += 1
                        index = k*bins_lon+l #matriz[i,j] -> vetor[i*45+j], i=lon, j=lat, i=k, j=l
                        
                        model.bins[index] += 1
                        k,l = 0,0
    return model

def newModel(definitions,initialvalue=0):
    """ Creates an empty model based on a set of definitions. 
    The initialvalue parameter determines the initial value of 
    the bins contained in the model, and can be used to create 
    "neutral" models (containing 1 in all bins)

    bins are the dimensional size for lat and long
    cells are the dimensional size for mag
    """
    ret = model()
    totalbins,totalcells = 1, 1
    
    for i in definitions:
        totalbins *= i['bins']
        totalcells *= i['cells']

    ret.mag=False

    ret.definitions = definitions
    # ret.bins = [initialvalue]*totalbins
    ret.bins = numpy.ndarray(shape=(totalbins), dtype='i')
    ret.bins.fill(initialvalue)

    return ret

#TODO: check the mag and real situation
def saveModelToFile(model, filename,real=False, year=-1, type = 'w'):
    """ 
    It saves the model to a specific file, both passed as arg
    """
    if model.mag==False:
        with open(filename, 'w') as f:
            f.write(str(model.bins))
            f.write("\n")
            f.write(str(model.definitions))
            f.write("\n")
            f.close()
    else:
        numpy.savetxt(filename, model.bins)
        with open(filename+"def.txt", 'w') as f:
            f.write(str(model.definitions))
            f.write("\n")
        f.close()  
        if real==False:
            if (year != -1):
                aux= str.rpartition(filename, year)
                filename = aux[0]
            with open(filename+"loglikelihood.txt", type) as f:
                f.write(str(model.loglikelihood))
                f.write("\n")
            f.close()   

#TODO: Use something safer than Eval (someday)
def loadModelFromFile(filename, withMag=True):
    """
    It Load the model to a specific file,  passed as arg
    """

    ret = model()
    if withMag==False:
        with open(filename, 'r') as f:
            ret.bins = eval(f.readline())
            ret.definitions = eval(f.readline())
        f.close()
    else:
        with open(filename+"def.txt", 'r') as f:
            ret.definitions = eval(f.readline())
        f.close()
        ret.bins = numpy.loadtxt(filename, dtype="f")

    return ret


#TODO: the args, check them
def simpleHibrid(model,fileMag,fileSaveCat):
"""
function to merge the etasGaModel generated by GA with the mag catalog from the R package SAPP 
"""

    model.magnitudeValues = numpy.zeros(shape=(len(model.bins),model.definitions[2]['cells']), dtype='f')
    finished = sum(model.bins)
    f = open(fileMag, 'r')


    quakes = []
    times = []

    for line in f:
        if line[1] == '"':
            continue

        tokens = line.split(',')

        mag = float(tokens[4])
        time = float(tokens[5])
        quakes.append(mag)
        times.append(time)

        i, quakesCount, number = 0, 0, 1
    while quakes != [] and number<finished:
        if i >= len(model.bins):
            break
        j=0 
        while j < len(quakes):
            if  model.bins[i] > quakesCount:
                index = findIndex(model, quakes[j])
                if model.magnitudeValues[i][index] == 0:
                    number += 1
                    model.magnitudeValues[i][index] = quakes.pop(j)
                    times.pop(j)
                    j=0
                    quakesCount+=1
                else:
                    quakes[j]+=0.1
            else:
                i+=1
                quakesCount = 0  
                break
            j+=1
    f.close()

    return model


def findIndex(model, mag):
    """
    This function finds the position of the bin given the mag and position of the list model
    """

    index = 0
    step_mag = model.definitions[2]['step']
    min_mag = model.definitions[2]['min']
    max_mag = model.definitions[2]['min'] + (model.definitions[2]['cells'] * model.definitions[2]['step'])
    cells_mag = model.definitions[2]['cells']

    for n in range(cells_mag):    
        cell = (step_mag * n) + min_mag
        if mag >= cell and mag < (cell+step_mag): 
            if (cell + step_mag) >= max_mag: #to avoid the last index to be out of limits
                index -= 1
            break
        index += 1
    return index

#TODO: it is incrising the number os quakes in line 344
def ideaRIinMmodels(model, nQuakes,steps=5):
    """
    This function distributes the aftershocks of a mainshock based on RI models ideas.
    The aftershocks are located up, down, left and right to the mainshock bin.
    """

    maxIndex = model.definitions[0]['bins']*model.definitions[1]['bins']*model.definitions[2]['bins']-1
    minIndex = 0
    row = model.definitions[0]['bins']

    dataBins, dataIndex = [],[]

    for bins,index in zip(model.bins, range(len(model.bins))):
        if bins > 1:
            dataBins.append(bins)
            dataIndex.append(index)

    for i,j in zip(range(len(dataBins)), range(len(dataIndex))):

        value = dataBins[i]
        index = dataIndex[j]

        for newTarget in range(steps):
            newTarget+=1
            value -= 1

            if nQuakes > value:
                nQuakes -= value
            else:
                value = nQuakes
            

            if value > 0:
                if index-newTarget >= minIndex:
                    model.bins[index-newTarget] += round(value/4)

                if index+newTarget <= maxIndex:
                    model.bins[index+newTarget] += round(value/4)

                if index + newTarget*row <= maxIndex:
                    model.bins[index + newTarget*row] += round(value/4)

                if index - newTarget*row >= minIndex:
                    model.bins[index - newTarget*row] += round(value/4)           

            else:
                break


def pdfOmoriUtsu(t2=30, c=0.003, p=1.3):
    """
    This is the omori utsu formula [g(t-ti)] in the PDF form
    It Analyze earthquake clustering features by using stochastic reconstruction/zhuang
    Is used to add geophysics information to the models
    """
    pdf_triggered = ((p-1)/c)*math.pow((1+t2/c),-p)
    return pdf_triggered


def quakesTriggered(magMain, magThreshold=3):
    """
    It scales realationship between the n of aftershocks and the size of the mainshock
    A = area in km2 connecting afteshock with the mag of the mainshock
    Utsu and Seki (1955) formula/yamanaka
    It analyzes earthquake clustering features by using stochastic reconstruction/zhuang
    """
    alpha = math.pow(magMain,-1)
    A = math.pow(math.e,1.02*magMain -4)
    
    k = A * math.exp(alpha*(magMain-magThreshold))
    return k

def sumTriggeredByDaysWithRI(model, year, fileEtasim, t2=30):
    """
    This function applies the pdfOmoriUtsu and quakesTriggered combined with the RI idea in a model
    """
    limitTo12(model)
    aftershocks = 0
    #this vinculates magnitude data from SAPP package with earthquakes from them models      
    model=simpleHibrid(model,fileEtasim,"../Zona/paper_exp/testeModelCatalog.txt")
    for (binOfmagMain,index) in zip(model.magnitudeValues,range(len(model.magnitudeValues))):
        for magMain in binOfmagMain:
            if magMain > 0: 
                for t in range(t2):
                    aftershocks += pdfOmoriUtsu(t2=t)*quakesTriggered(magMain)
    ideaRIinMmodels(model, aftershocks)
    aftershocks = 0
    return model

#TODO: I need to talk about this
#This was implemented to be used with Zechar code, but without this some models reach really HIGH values
def limitTo12(model):
    """
    It limits the number of earhtquake in a bin to a max of 12
    """
    for bins,index in zip(model.bins, range(len(model.bins))):
        if bins > 12:
            model.bins[index]=12

    return model


