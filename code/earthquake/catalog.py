""" This module reads and filter data from catalog files
A catalog is defined as a list of events. Each event is a list
of floats containing, in order, the following information:

Year, Month, Day, Hour, Minute, Second, Latitude, Longitude,
Magnitude, Depth
"""

import math
from datetime import datetime

JMA_keys = ("lon","lat","year","month","day","mag","depth","hour",
            "min","sec")
FNET_keys = ("year","month","day","hour","min","sec","lat","lon",
             "depth","mag","s1","s2","d1","d2","r1","r2","depth2",
             "mag2","var")


# stackexchange says that python dicts are super fast, so we are using them
# to store catalog information AND the column names. Might want to change this later.
# fnet has 19 columns, jma has 10 columns
def readFromFile(filename):
    """ Returns a catalog created from a JMA or FNET text file
    """
    f = open(filename,"r")
    keys = None
    ret = list()
    
    for line in f:
        if line[0] == '#':
            continue
        tokens = line.split()
        
        # test the file type if still undefined
        if keys == None:
            if len(tokens)==10:
                keys = JMA_keys
            else:
                keys = FNET_keys

        event = dict()
        for key,value in zip(keys,tokens):
            event[key] = float(value)
            
        seconds = int(math.modf(event["sec"])[1])
        miliseconds = int(math.modf(event["sec"])[0]*1000)
        event["datetime"] = datetime(int(event["year"]),int(event["month"]),int(event["day"]),
                                     int(event["hour"]),int(event["min"]),seconds,miliseconds)
            
        ret.append(event)
    return ret

def filter(catalog,filter):
    """ Reduces a catalog by removing events that do not match the filter
    """
    pass	
