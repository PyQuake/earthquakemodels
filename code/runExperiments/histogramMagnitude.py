import matplotlib.pyplot as plt
import models.model as model
import earthquake.catalog as catalog
from collections import OrderedDict

def histogramMagnitude(catalog_, region):
    """
    Creates the histogram of magnitudes by a given region.
    Saves the histogram to the follwing path ./code/Zona2/histograms/'+region+'/Magnitude Histogram of ' + str(year) + " " + region + '.png'
    Where region, year are given by the application
    From 2000 to 2011
    """
    definition = model.loadModelDefinition('../params/' + region + '.txt')
    catalogFiltred = catalog.filter(catalog_, definition)
    year = 2000
    while(year < 2012):
        data = dict()
        for i in range(len(catalogFiltred)):
            if catalogFiltred[i]['year'] == year and catalogFiltred[i]['lat'] > 34.8 and catalogFiltred[i][
                    'lat'] < 37.05 and catalogFiltred[i]['lon'] > 138.8 and catalogFiltred[i]['lon'] < 141.05:
                data[catalogFiltred[i]['mag']] = data.get(catalogFiltred[i]['mag'], 0) + 1
        b = OrderedDict(sorted(data.items()))
        plt.title('Histogram of ' + str(year) + " " + region)
        plt.bar(range(len(data)), b.values(), align='center')
        plt.xticks(range(len(data)), b.keys(), rotation=25)
        # print(b)
        axes = plt.gca()
        plt.savefig(
            '../Zona2/histograms/'+region+'/Magnitude Histogram of ' +
            str(year) +
            " " +
            region +
            '.png')
        del data
        year += 1

def main():
    """
    Calls function to plot a hitogram of magnitudes by region, based on JMA catalog
    """
    catalog_ = catalog.readFromFile('../data/jmacat_2000_2013.dat')
    region = "Kanto"
    histogramMagnitude(catalog_, region)

    region = "Kansai"
    histogramMagnitude(catalog_, region) 

    region = "Tohoku"
    histogramMagnitude(catalog_, region)   

    region = "EastJapan"
    histogramMagnitude(catalog_, region)

if __name__ == "__main__":
    main()
