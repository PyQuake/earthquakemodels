# "Definitions" is a list of dictionaries defined by the keys:
# {"key","min","step","bins"} where
# Key - is which value is used for this bin
# min - is the minimum value used
# step - is the size of the bin
# bins - is the number of bins in this dimension
import pymysql.cursors
# import datetime
import numpy
# from models.mathUtil import invertPoisson
from collections import Counter


class model(object):
    def __init__(self):
        self.prob = None
        self.bins = None
        self.time = 0
        self.definitions = None
        self.logbook = None
        self.loglikelihood = 0
        self.year = None
        self.modelName = None
        self.executionNumber = 0
        self.values4poisson = None


def newModel(definitions,initialvalue=0):
    """ Creates an empty model based on a set of definitions.
    The initialvalue parameter determines the initial value of
    the bins contained in the model, and can be used to create
    "neutral" models (containing 1 in all bins)
    bins are the dimensional size for lat and long
    cells are the dimensional size for mag
    """
    ret = model()
    totalbins = 1

    for i in definitions:
        totalbins *= i['bins']
    ret.definitions = definitions
    ret.bins = numpy.ndarray(shape=(totalbins), dtype='i')
    ret.bins.fill(initialvalue)
    ret.prob = numpy.ndarray(shape=(totalbins), dtype='i')
    ret.prob.fill(0.0)
    return ret

# This considers the catalog has passed a filter before
# TODO: Use datetime instead of year
# TODO: Redo this, this is terrible


def addFromCatalog(model,catalog, year):
    """
    Adds data from a catalog var to a model
    """

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
    # TODO: limpar isto um pouco
    for m in range(len(catalog)):
        #kind of a filter, we should define how we are going to filter by year
        if catalog[m]['year'] == year:  
            if catalog[m]['lon']>min_lon and catalog[m]['lon']<max_lon:
                if catalog[m]['lat']>min_lat and catalog[m]['lat']<max_lat:
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
                    k,l,cell_i = 0,0,0
    model.year=year
    return model
    

def loadModelDefinition(filename):
    """
    Creates a dictionary list with the definitions for a model from a file.
    The file is defined as multiple lines, with each line containing:
    key min step bins
    """
    f = open(filename, "r")
    ret = list()
    keys = ['key','min','step','bins', 'cells', 'max']
    
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


#TODO:choose a better name
#TODO: is used?This is used
#TODO: I do think theres a way to do this more phytonic
#Gen to Fen
def convertFromListToData(individual,length):
    """
    Function used to convert list model to GAModel configuration
    It finds the vinculates the list model positions in a bin and atribute a probability value to it
    """

    ret=model()
    ret.bins=[0]*length

    for gene in individual:    
        ret.bins[gene.index]=gene.prob

    return ret



def addFromCatalogP_AVR(model,catalog, riskMap, year):
    """
    This function adds the data from the geophysics models to the format used for the ga models.
    """
    k, l, index, cell, cell_i = 0, 0, 0, 0, 0

    values4poisson = [None] * (len(model.bins))

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
                    
                    
                    model.bins[index] += 1
                    k,l,cell_i = 0,0,0
                    
    
    k,l,cell_i, index = 0,0,0 ,0
    for element in riskMap:
        if element['lon'] > min_lon and element['lon'] < max_lon:
            if element['lat'] > min_lat and element['lat'] < max_lat:
                for i in range(bins_lon):    
                    index = (step_lon*i) + min_lon
                    if element['lon']>=index and element['lon']<(index+step_lon): 
                        if index+step_lon>max_lon: #to avoid the last index to be out of limits
                            k -= 1
                        break
                    k += 1
                for j in range(bins_lat):
                    index = (step_lat*j) + min_lat
                    if element['lat']>=index and element['lat']<(index+step_lat):
                        if index+step_lat>max_lat: #to avoid the last index to be out of limits
                            l -= 1
                        break
                    l += 1
                index = k*bins_lon+l #matriz[i,j] -> vetor[i*45+j], i=lon, j=lat, i=k, j=l

                if values4poisson[index] == None:
                    values4poisson[index] = list()
                if len(riskMap[0])!=11:
                    values4poisson[index].append(1 + element['prob'])
                else:
                    values4poisson[index].append(element['prob'])
                k,l,cell_i = 0,0,0

    for value, index in zip(values4poisson, range(len(values4poisson))):    
        if type(value) == type(list()):
            aux = Counter (value)
            prob = aux.most_common(1)
            values4poisson[index]= prob[0][0]

    for value, index in zip(values4poisson, range(len(values4poisson))):    
        if value == None: 
            j = bins_lon 
            i = bins_lat 
            neighbourVal = list()
            queue = list()
            queue.append(index)
            while True:
                pos = queue.pop()
                if pos < len(model.bins):
                    if (((pos+1) % j)!=0): #right
                        if values4poisson[pos+1] != None:
                            neighbourVal.append(values4poisson[pos+1])
                    if (pos >= j): #up
                        if values4poisson[pos-j] != None:
                            neighbourVal.append(values4poisson[pos-j])
                    if (pos < ((i*j)-j) and ((pos+1) % j)!=0): # dowm right
                        if values4poisson[(pos+j)+1] != None:
                            neighbourVal.append(values4poisson[(pos+j)+1])
                    if (pos < ((i*j)-j) and ((pos+1) % j)!=0): # down left 
                        if values4poisson[(pos+j) - 1] != None:
                            neighbourVal.append(values4poisson[(pos+j) - 1])
                    if (pos >= j and ((pos) % j)!=0): #up left
                        if values4poisson[(pos-j)-1] != None:
                            neighbourVal.append(values4poisson[(pos-j)-1])
                    if (pos >= j and ((pos+1) % j)!=0): # up right
                        if values4poisson[(pos-j)+1] != None:
                            neighbourVal.append(values4poisson[(pos-j)+1])
                    if (pos < (i*j)-j): #down
                        if values4poisson[pos+j] != None:
                            neighbourVal.append(values4poisson[pos+j])
                    if (((pos) % j)!=0): #left
                        if values4poisson[pos-1] != None:
                            neighbourVal.append(values4poisson[pos-1])
                    if neighbourVal != list() and queue == list():
                        values4poisson[index] = numpy.mean(neighbourVal)
                        break
                    elif queue == list():
                        queue.append(pos-j)
                        queue.append(pos-1)
                        queue.append(pos+1)
                        queue.append(pos+j)
                        
                    del queue
                    del neighbourVal


    model.values4poisson = values4poisson
    return model

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def saveModelDB(model):
    """ 
    It saves the model to a common database
    It is important to give a name to the model-> it will be used to load the model feom the db
    eg jmaData; GAModelKanto2000
    """
    # Connect to the database
    bins  = ','.join(str(x) for x in model.bins)
    definitions = str(model.definitions)
    modelName = model.modelName
    executionNumber = str(model.executionNumber)
    year = str(model.year)
    time = str(model.time)
    logbook = str(model.logbook)
    loglikelihood = str(model.loglikelihood)
    probability  = ','.join(str(x) for x in model.prob)
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='Fails158@featureless',
                                 db='earthquakemodelsDB',
                                 charset='utf8mb4',
                                 # unix_socket="/var/lib/mysql/mysql.sock",
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # Create a new record

            sql = "INSERT INTO `earthquakeModels` (`bins`, `definitions`, `modelName`, `year`, `time`, `logbook`, `loglikelihood` , `probability`, `executionNumber`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (bins, definitions, modelName, year, time, logbook, loglikelihood, probability, executionNumber))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
        print('Model saved...')
    except:
       # Rollback in case there is any error
       connection.rollback()
       print ("Error: unable to save model...")       

def loadModelDB(modelName, year, executionNumber=0):
    """ 
    It loads a model to a common database, using its name-> a variable indicanting what is this model
    eg jmaData; GAModelKanto2000
    """
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='Fails158@featureless',
                                 db='earthquakemodelsDB',
                                 charset='utf8mb4',
                                 # unix_socket="/var/lib/mysql/mysql.sock",
                                 cursorclass=pymysql.cursors.DictCursor)
    model_=model()
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM earthquakeModels WHERE modelName = '%s' AND executionNumber = '%s' AND year= '%s'" % (modelName, str(executionNumber), str(year))
            cursor.execute(sql)
            result = cursor.fetchall()
            for data in result:
                model_.bins = list(map(int, data['bins'].split(',')))
                model_.definitions = eval(data['definitions'])
                model_.modelName = data['modelName']
                model_.year = int(data['year'])
                model_.time = float(data['time'])
                model_.logbook = data['logbook']
                model_.loglikelihood = (data['loglikelihood'])
                model_.executionNumber = int(data['executionNumber'])
                model_.prob = list(map(float, data['probability'].split(',')))
                model_.bins=numpy.asarray(model_.bins, dtype='i')
                model_.prob=numpy.asarray(model_.prob, dtype='f')
    except:
        print ("Error: unable to fecth data")
    
    return model_

def showModelsDB(alldata=False):
    """ 
    It show all models to a common database, using its name-> a variable indicanting what is this model
    eg jmaData; GAModelKanto2000
    """
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='Fails158@featureless',
                                 db='earthquakemodelsDB',
                                 charset='utf8mb4',
                                 # unix_socket="/var/lib/mysql/mysql.sock",
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM earthquakeModels "
            cursor.execute(sql)
            result = cursor.fetchall()
            for data in result:
                if alldata==True:
                    print(data)
                    print('')
                else:
                    print("ModelName: %s and executionNumber: %s and year: %s" % (data['modelName'], data['executionNumber'], data['year']))

             
    except:
        print ("Error: unable to fecth data")


def removeModelDB(modelName, year, executionNumber):
    """ 
    It removes a model to a common database, using its name-> a variable indicanting what is this model
    eg jmaData; GAModelKanto2000
    """
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='Fails158@featureless',
                                 db='earthquakemodelsDB',
                                 charset='utf8mb4',
                                 # unix_socket="/var/lib/mysql/mysql.sock",
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM earthquakeModels WHERE modelName = '%s' AND executionNumber = '%s' AND year = '%s'" % (modelName, str(executionNumber), str(year))
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            connection.commit()
            print ("Model deleted...")
    except:
       # Rollback in case there is any error
       connection.rollback()
       print ("Error: unable to delete data")


def saveModelToFile(model, filename, real=False):
    """ 
    It saves the model to a specific file, both passed as arg
    """
    numpy.savetxt(filename, model.bins)
    with open(filename+"def", 'w') as f:
        f.write(str(model.definitions))
        f.write("\n")
        

#TODO: FIX THIS!!! For the mag=False situation
# Use something safer than Eval (someday)
def loadModelFromFile(filename):
    """
    It Load the model to a specific file,  passed as arg
    """

    ret = model()

    with open(filename+"def", 'r') as f:
        ret.definitions = eval(f.readline())
    f.close()
    ret.bins = numpy.loadtxt(filename, dtype="i")

    return ret


    