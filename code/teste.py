import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import models.model as model
import earthquake.catalog as catalog
from collections import OrderedDict
import numpy

# stats.register("std", numpy.std)


catalogo=catalog.readFromFile('../data/jmacat_2000_2013.dat')

data = dict()
data['0-25']=0
data['025-60']=0
data['060-100']=0
data['100-120']=0
data['120-150']=0
data['150-...']=0
list25, list60, list100, list120, list150, list180 = list(),list(),list(),list(),list(),list()
for i in range(len(catalogo)):
	# catalogo[i]['depth'] = int(catalogo[i]['depth'])
	if catalogo[i]['depth'] > 0 and catalogo[i]['depth'] < 25:
		data['0-25']+=1
		list25.append(catalogo[i]['depth'])
	elif catalogo[i]['depth'] > 25 and catalogo[i]['depth'] < 60:
		data['025-60']+=1
		list60.append(catalogo[i]['depth'])
	elif catalogo[i]['depth'] > 60 and catalogo[i]['depth'] < 100:
		data['060-100']+=1
		list100.append(catalogo[i]['depth'])
	elif catalogo[i]['depth'] > 100 and catalogo[i]['depth'] < 120:
		data['100-120']+=1
		list120.append(catalogo[i]['depth'])
	elif catalogo[i]['depth'] > 120 and catalogo[i]['depth'] < 150:
		data['120-150']+=1
		list150.append(catalogo[i]['depth'])
	elif catalogo[i]['depth'] > 150:
		data['150-...']+=1
		list180.append(catalogo[i]['depth'])

b = OrderedDict(sorted(data.items()))

plt.figure(figsize=(20, 10))
plt.title('[DEPTH]Histogram of earthquakes in Japan')
# plt.bar(range(len(data)), b.values(), align='center')
a = numpy.asarray(list25)
c = a.mean()
d = a.std()
plt.bar(0, b['0-25'], align='center', label='mean:'+str(c)+' std:'+str(d))
a = numpy.asarray(list60)
c = a.mean()
d = a.std()
plt.bar(1, b['025-60'], align='center', color='black', label='mean:'+str(c)+' std:'+str(d))
a = numpy.asarray(list100)
c = a.mean()
d = a.std()
plt.bar(2, b['060-100'], align='center', color='red', label='mean:'+str(c)+' std:'+str(d))
a = numpy.asarray(list120)
c = a.mean()
d = a.std()
plt.bar(3, b['100-120'], align='center', color='green', label='mean:'+str(c)+' std:'+str(d))
a = numpy.asarray(list150)
c = a.mean()
d = a.std()
plt.bar(4, b['120-150'], align='center', color='brown', label='mean:'+str(c)+' std:'+str(d))
a = numpy.asarray(list180)
c = a.mean()
d = a.std()
plt.bar(5, b['150-...'], align='center', color='blue', label='mean:'+str(c)+' std:'+str(d))
plt.xticks(range(len(data)), b.keys(), rotation=90, size=10)

plt.legend()

plt.savefig('../Zona2/histograms/Depth Histogram of earthquakes.png')

