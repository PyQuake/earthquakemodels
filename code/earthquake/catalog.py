""" This module reads and filter data from catalog files
A catalog is defined as a list of events. Each event is a list
of floats containing, in order, the following information:

Year, Month, Day, Hour, Minute, Second, Latitude, Longitude,
Magnitude, Depth
"""

#Implementantion notes:
# earthquakes is a list that contains the earthquake attributes
#I dont know if the names of the columns is going to be important in the future, so I added this info in the first element

# fnet has 19 columns, jma has 10 columns
def readFromFile(filename):
    """ Returns a catalog created from a JMA or FNET text file
    """
    f = open(filename,"r")

    earthquakes_JMA=['Lon Lat Year Month Day Mag_JMA Depth Hour Min Sec']
    earthquakes_FNET=['Year Month Day Hour Min Sec Lat Lon Depth Mag_JMA S1 S2 D1 D2 R1 R2 Depth Mag_FNET Var']

    # first, detecting JMA or FNET
    for line in f:
        if line[0] != '#':
            tokens = line.split()
            if (len(tokens)==10):
                #print ("JMA")
		del earthquakes_FNET[:]
		earthquakes_JMA.append(tokens)
            else:
                #print ("FNET")
		del earthquakes_JMA[:]
		earthquakes_FNET.append(tokens)

    if earthquakes_JMA != []:
         return earthquakes_JMA
    else:
         return earthquakes_JNET


def filter(catalog,filter):
    """ Reduces a catalog by removing events that do not match the filter
    """
    pass	
