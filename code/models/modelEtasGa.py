import rpy2.robjects as robjects
import datetime
import numpy
from models.mathUtil import invertPoisson

class model(object):
    pass

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
        # if definition['key'] == 'mag':
        #     range_mag = definition['step'] * definition['cells']
        #     step_mag = definition['step']
        #     min_mag = definition['min']
        #     max_mag = definition['min'] + (definition['cells'] * definition['step'])
        #     cells_mag = definition['cells']
    
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
    ret.bins = numpy.ndarray(shape=(totalbins), dtype='i')
    ret.bins.fill(initialvalue)

    return ret

def saveModelToFile(model, filename):
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
        ret.bins = numpy.loadtxt(filename, dtype="i")

    return ret