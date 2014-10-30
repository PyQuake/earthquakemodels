""" This module reads and filter data from catalog files
A catalog is defined as a list of events. Each event is a list
of floats containing, in order, the following information:

Year, Month, Day, Hour, Minute, Second, Latitude, Longitude,
Magnitude, Depth
"""

def readFromFile(filename):
    """ Returns a catalog created from a JMA or FNET text file
    """
    pass

def filter(catalog,filter):
    """ Reduces a catalog by removing events that do not match the filter
    """
    pass
