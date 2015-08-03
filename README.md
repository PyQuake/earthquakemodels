# earthquakemodels

Here is the code for generating Earthquake Risk Models using Genetic Algorithms. 

# Some Background

Some information outside the project frenquently used can be found at:
  
  http://www.corssa.org/articles/themevi/zechar
  
  http://www.cseptesting.org/
  
  https://github.com/stat157/background/issues/26
  
  http://www.jstor.org/stable/3085650?seq=2#page_scan_tab_contents

List of packages
-------------
The project uses the programming language Python, version 3.X.X. 
The python libraries used are:
sys
math
array
numpy
datetime
time
random
deap 

Getting Started
---------------


# Get the latest version
To get the last version you should clone the repository from gitHub to your local files.
```bash
git clone https://github.com/PyQuake/earthquakemodels.git

# How is the code organized
Most of the code were develop to be run in a python3 interpreter. You may find that some files can be bash executed.
In most cases, you can call the most important methods in two ways. The direct approach and the self-structured way. 

What i mean from direct approach: It is possible to simply call, for example, the method to genarate a model by GA. That method needs some arguments and you would have to provide them to be able to run the method. 

The self-structured way is an aprroach that allows you to call the method in the right sequence making it easier to run the methods.

# Executing the main GA methods - self-structured way
```bash
in applyGaModel.py you can generate some different kinds of GA models. All similar methods follows the same parttern: 
  in case you want to create the GA model based on some ETAS ideas, the you should run the following method:
    execEtasGaModel(year, times, save=False)
  you have to specify the year for the model and how many times you would like to execute the GA. Also, you may chose to save the model in a file. But first, you have to create the reference model for comparison (in most cases it is the resulting data after filtering the catalog by the year) by calling:
    createRealModelforEtas(year, save=False)
  with the same parameters, but times.
  
```
#Executing the main GA methods - The direct approach 
```bash
in the models.etasGaModelNP you can call the GA model method by itself. You may do it by:
  gaModel(NGEN,CXPB,MUTPB,modelOmega, year, n=500)
in which NGEN, CXPB, MUTPB and n are the GA parameters. modelOmega is the reference model to be comapared (in most cases it is the resulting data after filtering the catalog by the year). You should choose the year parameter as well.
```
Some tests were implemented. For those, the same idea above is applyed, we both have the The direct approach and the self-structured way. But in this case, the self-structured way is recommended. This may be out of date. 

```bash
in applyTests, it is possible to call the tests in two ways. The first one, execTests(year), executes all tests available for a group of comparesing models. Or it is possible to run the tests by itself as in execGamblingScore(year).
```

You may run he tests by their methods purely and all of them are or in testingAlarmBased.py or in loglikelihood.py. 

    
    
