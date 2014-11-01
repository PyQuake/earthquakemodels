# "definitions" list contains: [minimum value, total bins, step size]
# "bins" list contains the integer value for each bin

class model(object):
    pass

def newModel(definitions,initialvalue=0):
    """ Creates an empty model based on a set of definitions. 
    The initialvalue parameter determines the initial value of 
    the bins contained in the model, and can be used to create 
    "neutral" models (containing 1 in all bins)
    """
    ret = model()
    totalbins = 0
    for i in definitions:
        totalbins += definitions[i][1]
    ret.definitions = definitions
    ret.bins = [initialvalue]*totalbins
    return ret
    

def addCatalog(model,catalog):
    pass

def addEvent(model,event):
    pass
    
