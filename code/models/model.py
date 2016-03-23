# "Definitions" is a list of dictionaries defined by the keys: 
# {"key","min","step","bins"} where
# Key - is which value is used for this bin
# min - is the minimum value used
# step - is the size of the bin
# bins - is the number of bins in this dimension

#import rpy2.robjects as robjects
import datetime
import numpy
from models.mathUtil import invertPoisson

class model(object):
    pass

def newModel(definitions,mag=True,initialvalue=0):
    """ Creates an empty model based on a set of definitions. 
    The initialvalue parameter determines the initial value of 
    the bins contained in the model, and can be used to create 
    "neutral" models (containing 1 in all bins)

    bins are the dimensional size for lat and long
    cells are the dimensional size for mag
    """
    ret = model()
    totalbins,totalcells = 1, 1
    if mag==True:
        ret.mag=True
    else:
        ret.mag=False
    
    for i in definitions:
        totalbins *= i['bins']
        if ret.mag==True:
            totalcells *= i['cells']
        else:
            totalcells *= 1

    ret.definitions = definitions
    if ret.mag==True:
        ret.bins = numpy.ndarray(shape=(totalbins,totalcells), dtype='i')
        ret.bins.fill(initialvalue)
        ret.prob = numpy.ndarray(shape=(totalbins), dtype='i')
        ret.prob.fill(0.0)
    else:
        #This is how was done before
        # ret.bins = [initialvalue]*totalbins
        ret.bins = numpy.ndarray(shape=(totalbins), dtype='i')
        ret.bins.fill(initialvalue)
        ret.prob = numpy.ndarray(shape=(totalbins), dtype='i')
        ret.prob.fill(0.0)
    return ret
    

# This considers the catalog has passed a filter before
# TODO: Use datetime instead of year
def addFromCatalog(model,catalog, year):

    k, l, index, cell, cell_i = 0, 0, 0, 0, 0

    # TODO: nao usar key como nome de variavel aqui (criar um dicionario se necessario)
    # TODO: calcular o numero de keys in definition
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
        if definition['key'] == 'mag':
            range_mag = definition['step'] * definition['cells']
            step_mag = definition['step']
            min_mag = definition['min']
            max_mag = definition['min'] + (definition['cells'] * definition['step'])
            cells_mag = definition['cells']
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
                        
                        if model.mag==True:
                            if catalog[m]['mag']>min_mag and catalog[m]['mag']<max_mag:
                                #calculating the adequated bin for a coordinate of the mag of the quake
                                for n in range(cells_mag):    
                                    cell = (step_mag*n) + min_mag
                                    if catalog[m]['mag']>=cell and catalog[m]['mag']<(cell+step_mag): 
                                        if cell+step_mag>max_mag: #to avoid the last index to be out of limits
                                            cell_i -= 1
                                        break
                                    cell_i += 1

                                model.bins[index,cell_i] += 1
                        else:
                            model.bins[index] += 1
                        k,l,cell_i = 0,0,0
    return model
    

def loadModelDefinition(filename):
    """
    Creates a dictionary list with the definitions for a model from a file.
    The file is defined as multiple lines, with each line containing:
    key min step bins
    """
    f = open(filename, "r")
    ret = list()
    keys = ['key','min','step','bins', 'cells']
    
    for line in f:
        if line[0] == '#':
            continue
        tokens = line.split()
        definition = dict()
        for key,value in zip(keys,tokens):
            if key == 'key':
                definition[key] = value
            elif key == 'bins':
                definition[key] = int(value)
            elif key == 'cells':
                definition[key] = int(value)
            else:
                definition[key] = float(value)
        ret.append(definition)
        
    f.close()
    return ret

def saveModelToFile(model, filename, real=False):
    """ 
    It saves the model to a specific file, both passed as arg
    """
    numpy.savetxt(filename, model.bins)
    with open(filename+"def.txt", 'w') as f:
        f.write(str(model.definitions))
        f.write("\n")
    if real==False:
        with open(filename+"loglikelihood.txt", 'w') as f:
            f.write(str(model.loglikelihood))
            f.write("\n")
        f.close()   

#TODO: FIX THIS!!! For the mag=False situation
# Use something safer than Eval (someday)
def loadModelFromFile(filename):
    """
    It Load the model to a specific file,  passed as arg
    """

    ret = model()

    with open(filename+"def.txt", 'r') as f:
        ret.definitions = eval(f.readline())
    f.close()
    ret.bins = numpy.loadtxt(filename, dtype="f")

    return ret

def createImageFromModel(modelToDraw,fileToSave):
    robjects.r('''source("models/createMatrix.R")''')
    r_myfunction = robjects.globalenv['plotMatrixModel']
    modeldata = robjects.IntVector(modelToDraw.bins)
    r_myfunction(modeldata, fileToSave)   





#TODO: Check if this function really is obslote...
def convertMagtoNoMag(modelMag):
    """
    At first, you should use convert2DToArray
    Convert model (matrix) with mag array to a temporary model (array) without mag array
    It is important to use a different model to receive the return of this function
    """
    ret=model()

    ret.bins=[0]*len(modelMag.bins)
    for cell, i in zip(modelMag.bins, range(len(modelMag.bins))):
        ret.bins[i]=sum(cell)

    return ret

#TODO:Check if I sould add model.definitions to the returned model
def convert2DToArray(modelMag, definitions):
    """
    Convert model (matrix) with mag array to a model (array) with mag
    The new model is a 1D array
    It is important to use a different model to receive the return of this function

    IMPORTANT: The definition used here should be with Mag definitions
    """
    ret=model()

    ret.bins = numpy.ndarray(shape=(len(modelMag.bins)*len(modelMag.bins[0])), dtype='i')
    ret.bins.fill(0)

    ret.definitions=definitions
     
    i=0
    for bin in modelMag.bins:
        j=0
        while j<len(bin):
            ret.bins[i*j]=bin[j]
            j+=1
        i+=1
    return ret

def convertArrayto2D(modelWithout, definitions):
    """
    Convert model (array) with mag array to a model (matrix) with mag
    The new model is a 2D array
    It is important to use a different model to receive the return of this function

    IMPORTANT: The definition used here should be with Mag definitions
    """
    ret=model()
     
    totalbins,totalcells = 1, 1
    for i in definitions:
        totalbins *= i['bins']
        totalcells *= i['cells']
    ret.bins = numpy.ndarray(shape=(totalbins,totalcells), dtype='i')
    ret.bins.fill(0)

    ret.definitions=definitions
    ret.mag=True

    i,j=0,0
    for bin in modelWithout.bins:
        ret.bins[i,j]=bin
        j+=1
        i+=1
        if j==totalcells:
            j=0
        if i==totalbins:
            i=0

    return ret


#TODO:choose a better name
#Gen to Fen
def convertFromListToData(observations,length):

    ret=model()
    ret.bins=[0.0]*length

    for gene in observations:    
        ret.bins[gene.index]=gene.prob
    return ret

