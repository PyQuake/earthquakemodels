import matplotlib.pyplot as plt
import models.model as model
import earthquake.catalog as catalog
from collections import OrderedDict

def histogramEarthquakes(catalog_, region):
    """
    Creates the histogram of earthquake events by a given region.
    Saves the histogram to the follwing path ./code/Zona2/histograms/Kanto/earthquake in ' + region + '.png'
    Where region is given by the application
    From 2000 to 2013
    """
    definition = model.loadModelDefinition('../params/' + region + '.txt')
    catalog_ = catalog.filter(catalog_, definition)
    year = 2000
    data = dict()
    while(year <= 2013):
        for i in range(len(catalog_)):
            if catalog_[i]['year'] == year and catalog_[i]['lat'] > 34.8 and catalog_[i][
                    'lat'] < 37.05 and catalog_[i]['lon'] > 138.8 and catalog_[i]['lon'] < 141.05:
                data[year] = data.get(year, 0) + 1
        year += 1
    plt.title('Histogram of earthquake in' + region)
    plt.bar(range(len(data)), data.values(), align='center')
    plt.xticks(range(len(data)), data.keys(), rotation=25)
    axes = plt.gca()
    plt.savefig('../Zona2/histograms/Kanto/earthquake in ' + region + '.png')
    del data

def main():
    """
    Calls function to plot a hitogram of earthquakes events by region, based on JMA catalog
    """
    catalog_ = catalog.readFromFile('../data/jmacat_2000_2013.dat')
    
    region = "Kanto"
    histogramEarthquakes(catalog_, region):
    
    region = "Kansai"
    histogramEarthquakes(catalog_, region):

    region = "Tohoku"
    histogramEarthquakes(catalog_, region):


    region = "EastJapan"
    histogramEarthquakes(catalog_, region):

if __name__ == "__main__":
    main()
