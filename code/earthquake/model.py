# This module defines a module

class model(object):
    pass

def newModel():
    m = model()
    m.bins=[]
    m.definitions={}
    return m

def addDefinitions(model,definitions):
    model.definitons = definitons

def addCatalog(model,catalog):
    pass

def addEvent(model,event):
    pass

def appendDefinition(model,name,min,length,step):
    model.definition[name] = [min,length,step]
