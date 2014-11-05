# "Definitions" is a list of dictionaries defined by the keys: 
# {"key","min","step","bins"} where
# Key - is which value is used for this bin
# min - is the minimum value used
# step - is the size of the bin
# bins - is the number of bins in this dimension

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
    

def addCatalog(model,catalog):
    # TODO: everything
    ret = []
    for event in catalog:
        discarded = False
        for condition in conditions:
            if 'min' in condition:
                discarded = discarded or (event[condition['key']] < condition['min'])
            if 'max' in condition:
                discarded = discarded or (event[condition['key']] > condition['max'])
            if discarded:
                break
        if not discarded:
            ret.append(event)
    return ret
    
    
    
    pass

def loadModelDefinition(filename):
    """ Creates a dictionary list with the definitions for a model from a file.
    The file is defined as multiple lines, with each line containing:
    key min step bins
    """
    f = open(filename)
    ret = list()
    keys = {'key','min','step','bins'}
    
    for line in f:
        if line[0] == '#':
            continue
        tokens = line.split()
        definition = dict()
        for key,value in zip(keys,tokens):
            definition[key] = value
        ret.append(definition)
        
    f.close()
    return ret