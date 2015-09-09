print()
print()
print("In this file we explain how to use the earthquakemodels framework")
print()
print("We may want to create models using the GA models")
print("First we need to create our reference model")
print("Thats done by calling the applyGaModel and executing the methods as in the applyGaModel file")
print()
print("import applyGaModel")
# import applyGaModel

print("We have two kinds reference models. The first one is used by the simple GA model, the second one is used by the Hibrid GA model hibridization between the simple GA model and the ETAS model")
print("The first method can be used for creating reference models that takes into account magnitude, it has no return")
print("For learning reasons, its recommended to run it with the following parameters:")
print("2000 <= year <= 2010, withMag = False, save (to file) = False")
# print("Running: applyGaModel.createRealModel(year=2000, withMag=False, save=False)")
# applyGaModel.createRealModel(year=2000, withMag=False, save=False)
print("Finished")
print()
print("This second method is similar to the last one, but there isnt any option that considers magnitude, it has no return")
print("For learning reasons, its recommended to run it with the following parameters:")
print("2000 <= year <= 2010, save (to file) = False")
print("Running: applyGaModel.createRealModelforEtas(year=2000, save=False)")
# applyGaModel.createRealModelforEtas(year=2000, save=False)
print("Finished")
print()
print("The next methods can olny be executed if the previous ones have been completed with the parameter 'save = True'")
print("We are lucky and thats already done, so we can move foward")
print()
print("The first method can be used for creating simple GA models that takes into account only the locacality of the quakes")
print("For learning reasons, its recommended to run it with the following parameters:")
print("2000 <= year <= 2010, times = 1 (hence its non-stochastic, you may want to run it several times), save (to file) = False")
print("Running: applyGaModel.execGaModel(year=2000, times=1, save=False)")
# applyGaModel.execGaModel(year=2000, times=1, save=False)
print("Finished")
print()
print("The second method can be used for creating the hibrid between etas and simpleGA")
print("For learning reasons, its recommended to run it with the following parameters:")
print("2000 <= year <= 2010, times = 1 (hence its non-stochastic, you may want to run it several times), save (to file) = False")
print("Running: applyGaModel.execEtasGaModel(year=2000, times=1, save=False)")
# applyGaModel.execEtasGaModel(year=2000, times=1, save=False)
print("Finished")
print()
print("The last method can be used for creating the a extended version of the simpleGA that also takes into account magnitude")
print("For learning reasons, its recommended to run it with the following parameters:")
print("2000 <= year <= 2010, times = 1 (hence its non-stochastic, you may want to run it several times), save (to file) = False")
print("Running: applyGaModel.execGaModelWithMag(year=2000, times=1, save=False)")
# applyGaModel.execGaModelWithMag(year=2000, times=1, save=False)
print("Finished")
print()
print()
print("This ends the first part of the framework. The next one is about testing and comparing the models")
print()
print("For being able to do that, we need to call the methods in the applyTests file")

print("import applyTests")
import applyTests

print("We may execute the available tests. Those are the ASS test, the Gambling Score test, the L and N test.")
print("It is possible to calculate the log-Likelihood of the models and run the tests all at once")
print("For all tests, we used the parameter values as 2000 <= year <= 2010")
print("These tests only work for the simpleGA version")
print()
print("Running: applyTests.execAss(year=2000)")
# applyTests.execAss(year=2000)
print("Finished")
print("Running: applyTests.execGamblingScore(year=2000)")
# applyTests.execGamblingScore(year=2000)
print("Finished")
print("Running: applyTests.execLTest(year=2000)")
# applyTests.execLTest(year=2000)
print("Finished")
print("Running: applyTests.execNTest(year=2000)")
# applyTests.execNTest(year=2000)
print("Finished")
print("Running: applyTests.execLogLikelihood(year=2000)")
# applyTests.execLogLikelihood(year=2000)
print("Finished")


print("Later we found a way to use those tests in a different way. Zechar, in http://www.corssa.org/articles/themevi/zechar, implemetated most of the tests in Java.")
print("For convertion a one of our models to a struture capable of being used in Zechar's code, you should first:") 
print()
print("import models.modelEtasGa.py and load a model to convert (or use one of your own)")
import models.modelEtasGa as etasGA
print("Loading model to convert to zechars test structure.")
print("import models.modelEtasGA and do m=models.modelEtasGAloadModelFromFile('../Zona/etasNP2000exec.txt')")
print("OBS: If you can load a model, you can also save it by doing:")
print("modelEtasGA.saveModelFromFile(filename)")
m=etasGA.loadModelFromFile("../Zona/model/etasNP2000exec.txt")
print("Model loaded")
print("and then call modelToZecharTests(model, filename, startDate, endDate)")
print("The first two parameters are the most important ones. Model is the model that you want to convert and filename is the full path for where you want to save the new structured model. startDate and endDate are string values for the period, in years, of the model. ")
print("Running: modelToZecharTests(model, filename, startDate, endDate)")

print("Creating xml for Zechars tests...")
etasGA.modelToZecharTests(model=m, filename="../Zona/modelTestInZechar/manual.xml", startDate="2000", endDate="2001")
print("Finished")


print()


print("You may want to complete the simple hibridization made between the simpleGA model and the ETAS model")
print("For that you should study the R package sapp to be able to generate magnitude files using ETAS techniques")
print("Then you should used the imported package models.modelEtasGA and call the method simpleHidrid with the following parameters:")
print("model=modelo,fileMag='../Zona/etasim1.txt', fileSaveCat='../Zona/testeModelCatalog.txt')")
print("Start hibridization...")
hibrid=etasGA.simpleHibrid(model=m,fileMag="../Zona/etasim1.txt", fileSaveCat="../Zona/testeModelCatalog.txt")
print("Finished")












