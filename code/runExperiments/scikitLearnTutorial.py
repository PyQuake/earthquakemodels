# from __future__ import print_function

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.svm import SVC
import numpy as np
import sys
sys.path.insert(0, '..')
import models.model as model
import gaModel.gaModel_Yuri as ga


qntYears = 5
region = 'Kanto'
year=2000
times = 1

observations = list()
means = list()
logbook = list()
for i in range(qntYears):
    observation = model.loadModelDB(region+'jmaData', year+i)
    observation.bins = observation.bins.tolist()
    observations.append(observation)
    means.append(observation.bins)
del observation
mean = np.mean(means, axis=0)
labels = model.loadModelDB(region+'jmaData', year+i+1)

# (trainData, testData, trainLabels, testLabels) = train_test_split(
# 	observations, labels, test_size=0.25, random_state=42)

trainData = observations
trainLabels = labels

#aqui eu set o parametro k 
# Set the parameters by cross-validation
#select, tournament size, k [1-250]
tuned_parameters = [{'NGEN': [1-250]}]

clf = GridSearchCV(ga.gaModel(CXPB=0.9,MUTPB=0.1,modelOmega=observations,year=year+qntYears,
        region=region,mean=mean,n_aval=50), tuned_parameters)

clf.fit(trainData, trainLabels)

#outputing
print("Best parameters set found on development set:")
print()
print(clf.best_params_)
print()
print("Grid scores on development set:")
print()
means = clf.cv_results_['mean_test_score']
stds = clf.cv_results_['std_test_score']
for mean, std, params in zip(means, stds, clf.cv_results_['params']):
    print("%0.3f (+/-%0.03f) for %r"
          % (mean, std * 2, params))
print()
