import matplotlib.pyplot as plt
import models.model as model
import earthquake.catalog as catalog
from collections import OrderedDict

region = "Kanto"
definition = model.loadModelDefinition('../params/' + region + '.txt')
catalogo = catalog.readFromFile('../data/jmacat_2000_2013.dat')
catalogo = catalog.filter(catalogo, definition)
year = 2000
data = dict()
while(year <= 2013):
    for i in range(len(catalogo)):
        if catalogo[i]['year'] == year and catalogo[i]['lat'] > 34.8 and catalogo[i][
                'lat'] < 37.05 and catalogo[i]['lon'] > 138.8 and catalogo[i]['lon'] < 141.05:
            data[year] = data.get(year, 0) + 1
    year += 1
plt.title('Histogram of earthquake in' + region)
plt.bar(range(len(data)), data.values(), align='center')
plt.xticks(range(len(data)), data.keys(), rotation=25)
axes = plt.gca()
plt.savefig('../Zona2/histograms/Kanto/earthquake in ' + region + '.png')
del data

region = "Kansai"
definition = model.loadModelDefinition('../params/' + region + '.txt')
catalogo = catalog.readFromFile('../data/jmacat_2000_2013.dat')
catalogo = catalog.filter(catalogo, definition)
year = 2000
data = dict()
while(year <= 2013):
    for i in range(len(catalogo)):
        if catalogo[i]['year'] == year and catalogo[i]['lon'] > 134.5 and catalogo[
                i]['lon'] < 136.5 and catalogo[i]['lat'] > 34 and catalogo[i]['lat'] < 36:
            data[year] = data.get(year, 0) + 1
    year += 1
plt.title('Histogram of earthquake in' + region)
plt.bar(range(len(data)), data.values(), align='center')
plt.xticks(range(len(data)), data.keys(), rotation=25)
axes = plt.gca()
plt.savefig('../Zona2/histograms/Kansai/earthquake in ' + region + '.png')
del data

region = "Tohoku"
definition = model.loadModelDefinition('../params/' + region + '.txt')
catalogo = catalog.readFromFile('../data/jmacat_2000_2013.dat')
catalogo = catalog.filter(catalogo, definition)
year = 2000
data = dict()
while(year <= 2013):
    for i in range(len(catalogo)):
        if catalogo[i]['year'] == year and catalogo[i]['lon'] > 139.8 and catalogo[
                i]['lon'] < 141.8 and catalogo[i]['lat'] > 37 and catalogo[i]['lat'] < 41:
            data[year] = data.get(year, 0) + 1
    year += 1
plt.title('Histogram of earthquake in' + region)
plt.bar(range(len(data)), data.values(), align='center')
plt.xticks(range(len(data)), data.keys(), rotation=25)
axes = plt.gca()
plt.savefig('../Zona2/histograms/Tohoku/earthquake in ' + region + '.png')
del data


region = "EastJapan"
definition = model.loadModelDefinition('../params/' + region + '.txt')
catalogo = catalog.readFromFile('../data/jmacat_2000_2013.dat')
catalogo = catalog.filter(catalogo, definition)
year = 2000
data = dict()
while(year <= 2013):
    for i in range(len(catalogo)):
        if catalogo[i]['year'] == year and catalogo[i]['lon'] > 140 and catalogo[
                i]['lon'] < 144 and catalogo[i]['lat'] > 37 and catalogo[i]['lat'] < 41:
            data[year] = data.get(year, 0) + 1
    year += 1
plt.title('Histogram of earthquake in' + region)
plt.bar(range(len(data)), data.values(), align='center')
plt.xticks(range(len(data)), data.keys(), rotation=25)
axes = plt.gca()
plt.savefig('../Zona2/histograms/EastJapan/earthquake in ' + region + '.png')
del data
