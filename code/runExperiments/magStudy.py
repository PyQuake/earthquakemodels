# convert to R - doing

# do analysis -> t.test or anova? ANOVA

from csep.loglikelihood import calcLogLikelihood as loglikelihood
import gaModel.etasGaModelNP as etasGaModelNP
import models.model as model
import models.modelEtasGa as etasGa

"""
This file needs to be undestood -> what does it do?
"""

def loadModelSC(type, year, region, depth, i):
    if type == 'gaModel':
        filename = '../Zona3/scModel/gamodel' + region + '_' + \
            str(depth) + '_' + str(year) + str(i) + '.txt'
        modelo = etasGa.loadModelFromFile(filename)
    if type == 'sc_hybrid_gaModel':
        filename = '../Zona2/sc_hybrid_gaModel/hybrid_gaModel' + region + \
            '_' + str(depth) + '_' + str(year) + '_' + str(i) + '.txt'
        modelo = etasGa.loadModelFromFile(filename)
    if type == 'sc_hybrid_ListaGA_New':
        filename = '../Zona2/sc_hybrid_ListaGA_New/hybrid_ListaGA_New' + \
            region + '_' + str(depth) + '_' + str(year) + '_' + str(i) + '.txt'
        modelo = etasGa.loadModelFromFile(filename)
    elif region == 'EastJapan':
        filename = '../Zona3/scModel/eastgamodel' + region + \
            '_' + str(depth) + '_' + str(year) + str(i) + '.txt'
        modelo = etasGa.loadModelFromFile(filename)
    else:
        filename = '../Zona3/scModel/listgamodel' + region + \
            '_' + str(depth) + '_' + str(year) + str(i) + '.txt'
        modelo = etasGa.loadModelFromFile(filename)
    fileEtasim = "../Zona/paper_exp/etasim1.txt"
    modelo = etasGa.simpleHibrid(
        modelo,
        fileEtasim,
        "../Zona/paper_exp/testeModelCatalog.txt")
    return modelo


def saveModelSC(modelL, type, year, region, depth, i, minMag, maxMag):
    file = type.split('_')
    if type == 'gaModel':
        etasGa.saveModelToFile(
            modelL,
            '../Zona2/magStudy/gamodelSC/' +
            region +
            '_' +
            str(depth) +
            '_' +
            str(year) +
            str(i) +
            '_' +
            str(minMag) +
            ".txt")
    if type == 'sc_hybrid_gaModel':
        filename = "../Zona2/dataForR/magStudy/sc_hybrid_gaModel/" + region + \
            "_" + str(depth) + "_" + str(year) + '_' + str(minMag) + ".txt"
    if type == 'sc_hybrid_ListaGA_New':
        filename = "../Zona2/dataForR/magStudy/sc_hybrid_ListaGA_New/" + region + \
            "_" + str(depth) + "_" + str(year) + '_' + str(minMag) + ".txt"
    else:
        etasGa.saveModelToFile(
            modelL,
            '../Zona2/magStudy/listgamodel/' +
            region +
            '_' +
            str(depth) +
            '_' +
            str(year) +
            str(i) +
            '_' +
            str(minMag) +
            ".txt")


def calcLogLikelihoodMagInterval(region, year, year_end, modelL):
    modelO = model.loadModelFromFile(
        '../Zona2/realData/' +
        region +
        'real' +
        "_" +
        str(year) +
        '.txt')
    modelL.loglikelihood = loglikelihood(modelL, modelO)

    return modelL


def filterMag(modelo, minMag, maxMag):
    modelTemp = etasGa.newModel(modelo.definitions, 1)
    for magValues, bins, index in zip(
            modelo.magnitudeValues, modelo.bins, range(len(modelo.bins))):
        for mag in magValues:
            if mag > 0:
                if (minMag < mag and mag < maxMag):
                    modelTemp.bins[index] += 1
    return modelTemp


def converter2leastBest(type, region, depth, minMag,
                        maxMag, year_begin, year_end):

    file = type.split('_')

    year = year_begin
    while(year <= year_end):
        data = list()
        for i in range(10):
            if type == 'gaModel':
                filename = '../Zona2/magStudy/gamodelSC/' + region + '_' + \
                    str(depth) + '_' + str(year) + str(i) + '_' + \
                    str(minMag) + ".txtloglikelihood.txt"
            else:
                filename = '../Zona2/magStudy/listgamodel/' + region + '_' + \
                    str(depth) + '_' + str(year) + str(i) + '_' + \
                    str(minMag) + ".txtloglikelihood.txt"
                if region == 'EastJapan':
                	filename = '../Zona2/magStudy/eastgamodel/'+region+'_'+str(depth)+'_'+str(year)+str(i)+'_'+str(minMag)+".txtloglikelihood.txt"
            if (file[0] == 'clustered' or file[0] == 'clusteredII'):
            	if len(file) == 4:#new
            		filename = "../Zona2/magStudy/"+type+'/'+file[1]+'_'+file[2]+'_'+file[3]+region+"_"+str(depth)+"_"+str(year)+'_'+str(i)+'_'+str(minMag)+".txtloglikelihood.txt"
            	elif file[1] == 'hybrid':
            		filename ="../Zona2/magStudy/"+type+'/'+file[1]+'_'+file[2]+'_'+region+"_"+str(depth)+"_"+str(year)+'_'+str(i)+'_'+str(minMag)+".txtloglikelihood.txt"
            	else:
            		filename = "../Zona2/magStudy/"+type+'/'+region+"_"+str(depth)+"_"+str(year)+'_'+str(i)+'_'+str(minMag)+".txtloglikelihood.txt"
            elif (file[0] == 'hybrid'):
            	filename = "../Zona2/magStudy/"+type+'/'+type+region+"_"+str(depth)+"_"+str(year)+'_'+str(i)+'_'+str(minMag)+".txtloglikelihood.txt"
            else:
            	filename = "../Zona2/magStudy/"+type+'/'+region+"_"+str(depth)+"_"+str(year)+str(i)+'_'+str(minMag)+".txtloglikelihood.txt"

            f = open(filename, "r")
            for line in f:
                info = line.split()
                data.append(float(info[0]))
            f.close()

        if type == 'gaModel':
            filename = "../Zona2/dataForR/magStudy/gamodelSC/" + region + \
                "_" + str(depth) + "_" + str(year) + '_' + str(minMag) + ".txt"
        if type == 'sc_hybrid_gaModel':
            filename = "../Zona2/dataForR/magStudy/sc_hybrid_gaModel/" + region + \
                "_" + str(depth) + "_" + str(year) + '_' + str(minMag) + ".txt"
        if type == 'sc_hybrid_ListaGA_New':
            filename = "../Zona2/dataForR/magStudy/sc_hybrid_ListaGA_New/" + region + \
                "_" + str(depth) + "_" + str(year) + '_' + str(minMag) + ".txt"
        else:
            filename = "../Zona2/dataForR/magStudy/listgamodel/" + region + \
                "_" + str(depth) + "_" + str(year) + '_' + str(minMag) + ".txt"
        with open(filename, 'w') as f:
            for i in range(10):
                f.write(str(data[i]))
                f.write("\n")
        year += 1


def main():
    print('filtering')
    depth = 100
    types = (
        'sc_hybrid_gaModel',
        'sc_hybrid_ListaGA_New',
        'gaModel',
        'listaGA_new')
    regions = ('EastJapan', 'Kansai', 'Kanto', 'Tohoku')
	year_end=2010
	for region in regions:
		for t in types:
			year=2005
			while(year<=year_end):
				minMag = 3.0
				while minMag<= 9.0:
					maxMag = minMag + 1.0
					for numExec in range(10):
						modelo=loadModelSC(t, year, region, depth=depth, i=numExec)
						modelo = filterMag(modelo, minMag=minMag, maxMag=maxMag)
						modelo=calcLogLikelihoodMagInterval(region, year=year, year_end=year_end, modelL=modelo)
						saveModelSC(modelo,t, year, region, depth, numExec, minMag, maxMag)
					minMag=minMag+1.0
				year+=1
    print('converting')
    types = (
        'sc_hybrid_gaModel',
        'sc_hybrid_ListaGA_New',
        'gaModel',
        'listaGA_new')
    for region in regions:
        for t in types:
            minMag = 3.0
            while minMag <= 9.0:
                maxMag = minMag + 1.0
                converter2leastBest(
                    t,
                    region,
                    depth,
                    minMag,
                    maxMag,
                    year_begin=2005,
                    year_end=2010)
                minMag = minMag + 1.0

if __name__ == "__main__":
    main()
