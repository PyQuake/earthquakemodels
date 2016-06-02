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

def addFromCatalog(model,catalog, year):

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

def saveModelToFile(model, filename,real=False):
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
            with open(filename+"loglikelihood.txt", 'w') as f:
                f.write(str(model.loglikelihood))
                f.write("\n")
            f.close()   
        # with open(filename+"prob.txt", 'w') as f:
        #     f.write(str(model.prob))
        #     f.write("\n")
        # f.close()   

# Use something safer than Eval (someday)
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
        # with open(filename+"prob.txt", 'r') as f:
        #     ret.prob = eval(f.readline())
        # f.close()
        ret.bins = numpy.loadtxt(filename, dtype="f")

    return ret



#function to merge the etasGaModel generated by GA with the mag catalog from the R package SAPP 
def simpleHibrid(model,fileMag,fileSaveCat):

    # modelo=etasGa.loadModelFromFile('../Zona/model/etasNP2000exec.txt')

    model.magnitudeValues = numpy.zeros(shape=(len(model.bins),model.definitions[2]['cells']), dtype='f')
    finished = sum(model.bins)
    # f = open("../Zona/etasim1.txt", 'r')
    f = open(fileMag, 'r')

    # g = open("./testeModelCatalog.txt", 'w')
    g = open(fileSaveCat, 'w')
    g.write("#no.   longitude   latitude    magnitude   time    depth   year    month   days")
    g.write("\n")
    g.close()

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
        j = 0 
        while j < len(quakes):
            if  model.bins[i] > quakesCount:
                index = localizarIndex(model, quakes[j])
                if model.magnitudeValues[i][index] == 0:
                    saveCatalog(fileSaveCat, model, i, number, quakes[j], times[j])
                    number += 1

                    model.magnitudeValues[i][index] = quakes.pop(j)
                    times.pop(j)

                    j = 0
                    quakesCount+=1
                else:
                    quakes[j]+=0.1
            else:
                i+=1
                quakesCount = 0  
                break
            j+=1
    f.close()
    g.close()
    return model

def saveCatalog(fileSaveCat, modelo, index, number, mag, time):
    lon, lat = calcCoordenada(modelo, index)
    depth, year, month, days = 0,0,0,0
    data2Save = []
    data2Save.append(number)
    data2Save.append(lon)
    data2Save.append(lat)
    data2Save.append(mag)
    data2Save.append(time)
    data2Save.append(depth)
    data2Save.append(year)
    data2Save.append(month)
    data2Save.append(days)

    f = open(fileSaveCat, 'a')
    f.write(str(data2Save))
    f.write("\n")
    f.close()

def calcCoordenada(modelo, index):

    newIndex = int(index / modelo.definitions[1]['bins'])
    lon = round(modelo.definitions[1]['step'] * newIndex + modelo.definitions[1]['min'],2)

    newIndex = index % modelo.definitions[0]['bins']
    lat = round(modelo.definitions[0]['step'] * newIndex + modelo.definitions[0]['min'],2)


    return lon, lat


def localizarIndex(modelo, mag):

    j = 0

    step_mag = modelo.definitions[2]['step']
    min_mag = modelo.definitions[2]['min']
    max_mag = modelo.definitions[2]['min'] + (modelo.definitions[2]['cells'] * modelo.definitions[2]['step'])
    cells_mag = modelo.definitions[2]['cells']

    for n in range(cells_mag):    
        cell = (step_mag * n) + min_mag
        if mag >= cell and mag < (cell+step_mag): 
            if (cell + step_mag) >= max_mag: #to avoid the last index to be out of limits
                j -= 1
            break
        j += 1
    return j


def modelToZecharTests(model, filename, startDate, endDate):
    """
    Conversion between the model used by this framework to the template needed by zechar files.

    """

    startDate=startDate+"T"+str(00).zfill(2)+":"+str(00).zfill(2)+":"+str(00).zfill(2)+"Z"
    endDate=endDate+"T"+str(00).zfill(2)+":"+str(00).zfill(2)+":"+str(00).zfill(2)+"Z"

    with open(filename, 'w') as f:
        f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
        f.write("<CSEPForecast xmlns='http://www.scec.org/xml-ns/csep/forecast/0.05'>\n")
        f.write("  <forecastData publicID='smi:org.scec/csep/forecast/1'>\n")
        f.write("    <modelName>gaModel-UnB_Tsukuba</modelName>\n")
        f.write("    <version>1.0</version>\n")
        f.write("    <author>PyQuake-https://github.com/PyQuake/earthquakemodels</author>\n")

        now = datetime.datetime.now()
        f.write("    <issueDate>"+str(now.year)+"-"+str(now.month).zfill(2)+"-"+str(now.day).zfill(2)+
            "T"+str(now.hour).zfill(2)+":"+str(now.minute).zfill(2)+":"+str(00).zfill(2)+"Z</issueDate>\n")
        f.write("    <forecastStartDate>"+startDate+"</forecastStartDate>\n")
        f.write("    <forecastEndDate>"+endDate+"</forecastEndDate>\n")
        f.write("    <defaultCellDimension latRange='"+str(model.definitions[0]['step'])+
                                        "' lonRange='"+str(model.definitions[1]['step'])+"'/>\n")
        f.write("    <defaultMagBinDimension>"+str(model.definitions[2]['step'])+"</defaultMagBinDimension>\n")
        f.write("    <lastMagBinOpen>1</lastMagBinOpen>\n")
        f.write("    <depthLayer max='100.0' min='0.0'>\n")

        latSteps,longSteps, magSteps=0,0,0

        #Normalized or probability?
        binsNormalized = mathUtil.normalize(model.bins)
        # for bins in model.prob:
        for bins in binsNormalized:
            f.write("      <cell lat='"+str(round(model.definitions[0]['min']+latSteps*model.definitions[0]['step'],2))+
                                "' lon='"+str(round(model.definitions[1]['min']+longSteps*model.definitions[1]['step'],2))+"'>\n")
            f.write("        <bin m='"+str(round(model.definitions[2]['min']+magSteps*model.definitions[2]['step'],2))+
                                                    "'>"+str(bins)+"</bin>\n")
            # for num in bins:
            #     f.write("        <bin m='"+str(round(model.definitions[2]['min']+magSteps*model.definitions[2]['step'],2))+
            #                                         "'>"+str(num)+"</bin>\n")
            #     magSteps+=1

            f.write("      </cell>\n")

            latSteps+=1
            magSteps=0
            if latSteps==model.definitions[0]['bins']:
                latSteps=0
                longSteps+=1

        f.write("    </depthLayer>\n")
        f.write("  </forecastData>\n")
        f.write("</CSEPForecast>\n")

    f.close()

#TODO: it is incrising the number os quakes in line 344
def ideaRIinMmodels(model, nQuakes,steps=5):


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

        # number=pdfOmoriUtsu(t2=2)
        # k=quakesTriggered(random.uniform(0,8.5),3)
        # nQuakes = int(number*k)
        # if nQuakes>12:
        #     nQuakes=12

        for newTarget in range(steps):
            newTarget+=1
            value -= 2

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
    # g(t-ti)
    #Analyzing earthquake clustering features by using stochastic reconstruction/zhuang
    pdf_triggered = ((p-1)/c)*math.pow((1+t2/c),-p)
    return pdf_triggered


def quakesTriggered(magMain, magThreshold=3):
    alpha = math.pow(magMain,-1)
    #scaling realationship between the n of aftershocks and the size of the mainshock
    #A = area in km2 connecting afteshock with the mag of the mainshock
    #Utsu and Seki (1955) formula/yamanaka
    A = math.pow(math.e,1.02*magMain -4)
    #Analyzing earthquake clustering features by using stochastic reconstruction/zhuang
    k = A * math.exp(alpha*(magMain-magThreshold))
    return k

def sumTriggeredByDaysWithRI(model, year, fileEtasim, t2=30):
    limitTo12(model)
    aftershocks = 0
    model=simpleHibrid(model,fileEtasim,"../Zona/paper_exp/testeModelCatalog.txt")
    for (binOfmagMain,index) in zip(model.magnitudeValues,range(len(model.magnitudeValues))):
            for magMain in binOfmagMain:
                if magMain > 0: 
                    for t in range(t2):
                        aftershocks += pdfOmoriUtsu(t2=t+1)*quakesTriggered(magMain)
    ideaRIinMmodels(model, aftershocks)
    aftershocks = 0
    return model


def gutenbergRichterLaw(magMain, magThreshold=3, beta=1):
    return beta*math.pow(math.e,-beta*(magMain-magThreshold))

def limitTo12(model):
    for bins,index in zip(model.bins, range(len(model.bins))):
        if bins > 12:
            model.bins[index]=12

    return model


