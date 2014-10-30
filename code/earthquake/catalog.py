""" This module reads and filter data from catalog files
A catalog is defined as a list of events. Each event is a list
of floats containing, in order, the following information:

Year, Month, Day, Hour, Minute, Second, Latitude, Longitude,
Magnitude, Depth
"""

# fnet has 19 columns, jma has 10 columns
def readFromFile(filename):
    """ Returns a catalog created from a JMA or FNET text file
    """
    f = open(filename,"r")

    # first, detecting JMA or FNET
    for line in f:
        if line[0] != '#':
            tokens = line.split()
            if (len(tokens)==10):
                print ("JMA")
            else:
                print ("FNET")
            return


def filter(catalog,filter):
    """ Reduces a catalog by removing events that do not match the filter
    """
    pass
