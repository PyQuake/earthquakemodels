# "Definitions" is a list of dictionaries defined by the keys: 
# {"key","min","step","bins"} where
# Key - is which value is used for this bin
# min - is the minimum value used
# step - is the size of the bin
# bins - is the number of bins in this dimension

import rpy2.robjects as robjects

class model(object):
    pass

def newModel(definitions,initialvalue=0):
    """ Creates an empty model based on a set of definitions. 
    The initialvalue parameter determines the initial value of 
    the bins contained in the model, and can be used to create 
    "neutral" models (containing 1 in all bins)
    """
    ret = model()
    totalbins = 1
    for i in definitions:
        totalbins *= i['bins']
    ret.definitions = definitions
    ret.bins = [initialvalue]*totalbins
    return ret
    

# This considers the catalog has passed a filter before
# TODO: Use datetime instead of year
def addFromCatalog(model,catalog, year):

    k, l, index = 0, 0, 0

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

    # TODO: limpar isto um pouco
    for m in range(len(catalog)):
        #kind of a filter, we should define how we are going to filter by year
        if catalog[m]['year'] == year:  
            if catalog[m]['lon']>min_lon and catalog[m]['lon']<max_lon:
                if catalog[m]['lat']>min_lat and catalog[m]['lat']<max_lat:
                    #calculating the adequated bin for a coordinate of a earthquake
                    for i in range(bins_lon):    
                        index = (step_lon*i) + min_lon
                        if catalog[m]['lon']>=index and catalog[m]['lon']<(index+step_lon) : 
                            if index+step_lon>max_lon: #to avoid the last index to be out of limits
                                k -= 1
                            break
                        k += 1
                    for j in range(bins_lat):
                        index = (step_lat*j) + min_lat
                        if catalog[m]['lat']>=index and catalog[m]['lat']<(index+step_lat) :
                            if index+step_lat>max_lat: #to avoid the last index to be out of limits
                                l -= 1
                            break
                        l += 1
                    if(k==0 and l==0):
                        print (catalog[m]['lon'], catalog[m]['lat'])
                    index = k*bins_lon+l #matriz[i,j] -> vetor[i*45+j], i=lon, j=lat, i=k, j=l
                    model.bins[index] += 1
                    k,l = 0,0
    return model
    

def loadModelDefinition(filename):
    """
    Creates a dictionary list with the definitions for a model from a file.
    The file is defined as multiple lines, with each line containing:
    key min step bins
    """
    f = open(filename, "r")
    ret = list()
    keys = ['key','min','step','bins']
    
    for line in f:
        if line[0] == '#':
            continue
        tokens = line.split()
        definition = dict()
        for key,value in zip(keys,tokens):
            if key == 'key':
                definition[key] = value
            elif(key == 'bins'):
                definition[key] = int(value)
            else:
                definition[key] = float(value)
        ret.append(definition)
        
    f.close()
    return ret

def saveModelToFile(model, filename):
    """ Saves the model to a specific file, both passed as arg
    """

    with open(filename, 'w') as f:
        f.write(str(model.bins))
        f.write("\n")
        f.write(str(model.definitions))
        f.write("\n")
    f.close()
    #print ("The model was succesfully saved to the file", filename)

# Use something safer than Eval (someday)
def loadModelFromFile(filename):
    """
    Loads the model to a specific file,  passed as arg
    """

    ret = model()

    with open(filename, 'r') as f:
        ret.bins = eval(f.readline())
        ret.definitions = eval(f.readline())
    f.close()

    return ret

def createImageFromModel(modelToDraw,fileToSave):
    robjects.r('''source("models/createMatrix.R")''')
    r_myfunction = robjects.globalenv['plotMatrixModel']
    modeldata = robjects.IntVector(modelToDraw.bins)
    r_myfunction(modeldata, fileToSave)   
