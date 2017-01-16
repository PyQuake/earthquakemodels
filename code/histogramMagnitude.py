import matplotlib.pyplot as plt
import models.model as model
import earthquake.catalog as catalog
from collections import OrderedDict

region = "Kanto"
definition = model.loadModelDefinition('../params/' + region + '.txt')
catalogo = catalog.readFromFile('../data/jmacat_2000_2013.dat')
catalogo = catalog.filter(catalogo, definition)
year = 2000
while(year < 2012):
    data = dict()
    for i in range(len(catalogo)):
        if catalogo[i]['year'] == year and catalogo[i]['lat'] > 34.8 and catalogo[i][
                'lat'] < 37.05 and catalogo[i]['lon'] > 138.8 and catalogo[i]['lon'] < 141.05:
            data[catalogo[i]['mag']] = data.get(catalogo[i]['mag'], 0) + 1
    b = OrderedDict(sorted(data.items()))
    plt.title('Histogram of ' + str(year) + " " + region)
    plt.bar(range(len(data)), b.values(), align='center')
    plt.xticks(range(len(data)), b.keys(), rotation=25)
    # print(b)
    axes = plt.gca()
    plt.savefig(
        '../Zona2/histograms/Kanto/Magnitude Histogram of ' +
        str(year) +
        " " +
        region +
        '.png')
    del data
    year += 1

region = "Kansai"
definition = model.loadModelDefinition('../params/' + region + '.txt')
catalogo = catalog.readFromFile('../data/jmacat_2000_2013.dat')
catalogo = catalog.filter(catalogo, definition)
year = 2000
while(year < 2012):
    data = dict()
    for i in range(len(catalogo)):
        if catalogo[i]['year'] == year and catalogo[i]['lon'] > 134.5 and catalogo[
                i]['lon'] < 136.5 and catalogo[i]['lat'] > 34 and catalogo[i]['lat'] < 36:
            data[catalogo[i]['mag']] = data.get(catalogo[i]['mag'], 0) + 1
    b = OrderedDict(sorted(data.items()))
    plt.title('Histogram of ' + str(year) + " " + region)
    plt.bar(range(len(data)), b.values(), align='center')
    plt.xticks(range(len(data)), b.keys(), rotation=25)
    # print(b)
    axes = plt.gca()
    plt.savefig(
        '../Zona2/histograms/Kansai/Histogram of ' +
        str(year) +
        " " +
        region +
        '.png')
    del data
    year += 1

region = "Tohoku"
definition = model.loadModelDefinition('../params/' + region + '.txt')
catalogo = catalog.readFromFile('../data/jmacat_2000_2013.dat')
catalogo = catalog.filter(catalogo, definition)
year = 2000
while(year < 2012):
    data = dict()
    for i in range(len(catalogo)):
        if catalogo[i]['year'] == year and catalogo[i]['lon'] > 139.8 and catalogo[
                i]['lon'] < 141.8 and catalogo[i]['lat'] > 37 and catalogo[i]['lat'] < 41:
            data[catalogo[i]['mag']] = data.get(catalogo[i]['mag'], 0) + 1
    b = OrderedDict(sorted(data.items()))
    plt.title('Histogram of ' + str(year) + " " + region)
    plt.bar(range(len(data)), b.values(), align='center')
    plt.xticks(range(len(data)), b.keys(), rotation=25)
    # print(b)
    axes = plt.gca()
    plt.savefig(
        '../Zona2/histograms/Tohoku/Histogram of ' +
        str(year) +
        " " +
        region +
        '.png')
    del data
    year += 1


region = "EastJapan"
definition = model.loadModelDefinition('../params/' + region + '.txt')
catalogo = catalog.readFromFile('../data/jmacat_2000_2013.dat')
catalogo = catalog.filter(catalogo, definition)
year = 2000
while(year < 2012):
    data = dict()
    for i in range(len(catalogo)):
        if catalogo[i]['year'] == year and catalogo[i]['lon'] > 140 and catalogo[
                i]['lon'] < 144 and catalogo[i]['lat'] > 37 and catalogo[i]['lat'] < 41:
            data[catalogo[i]['mag']] = data.get(catalogo[i]['mag'], 0) + 1
    b = OrderedDict(sorted(data.items()))
    plt.title('Histogram of ' + str(year) + " " + region)
    plt.bar(range(len(data)), b.values(), align='center')
    plt.xticks(range(len(data)), b.keys(), rotation=25)
    # print(b)
    axes = plt.gca()
    plt.savefig(
        '../Zona2/histograms/EastJapan/Histogram of ' +
        str(year) +
        " " +
        region +
        '.png')
    del data
    year += 1
