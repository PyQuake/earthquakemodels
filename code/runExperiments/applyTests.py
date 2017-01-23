# depois fazer um arquivo na raiz para rodar todos os testes sobre os modelos
import models.model as model
import csep.loglikelihood as log
import models.randomModel as randomModel
import testingAlarmBased.molchanBased as molchanBased
from models.mathUtil import calcNumberBins
import testingAlarmBased.gamblingScore as gambling

def execGamblingScore(year):
    """
    Calculates the Gambling Score
    of the Models: GAModel, RandomModel
    """
    gaModel = model.loadModelFromFile('../Zona/modelo' + str(year) + '.txt')
    modeloReal = model.loadModelFromFile('../Zona/real' + str(year) + '.txt')

    unskilledModel = model.newModel(modeloReal.definitions)
    randomModel.makeRandomModel(unskilledModel)
    unskilledModel.bins = calcNumberBins(unskilledModel.bins, modeloReal.bins)

    gaGamblingScore = gambling.calcGamblingScore(gaModel, modeloReal)
    unskilledGamblingScore = gambling.calcGamblingScore(
        unskilledModel, modeloReal)

    print(gaGamblingScore)
    print(unskilledGamblingScore)


def execAss(year):
    """
    Calculates the ASS Test
    of the Models: GAModel, RandomModel
    """
    gaModel = model.loadModelFromFile('../Zona/modelo' + str(year) + '.txt')
    modeloReal = model.loadModelFromFile('../Zona/real' + str(year) + '.txt')

    unskilledModel = model.newModel(modeloReal.definitions)
    randomModel.makeRandomModel(unskilledModel)
    unskilledModel.bins = calcNumberBins(unskilledModel.bins, modeloReal.bins)

    gaModelValue = molchanBased.assTest(gaModel, modeloReal)
    unskilledModelValue = molchanBased.assTest(unskilledModel, modeloReal)

    print(gaModelValue)
    print(unskilledModelValue)


def execLTest(year):
    """
    Calculates the LTest
    of the Models: GAModel, RandomModel
    """
    gaModel = model.loadModelFromFile('../Zona/modelo' + str(year) + '.txt')
    modeloReal = model.loadModelFromFile('../Zona/real' + str(year) + '.txt')

    unskilledModel = model.newModel(modeloReal.definitions)
    randomModel.makeRandomModel(unskilledModel)
    unskilledModel.bins = calcNumberBins(unskilledModel.bins, modeloReal.bins)

    gaLTestValue = log.calcLTest(gaModel, modeloReal)
    unskilledLTestValue = log.calcLTest(unskilledModel, modeloReal)

    print(galTestValue)
    print(unskilledlTestValue)


def execNTest(year):
    """
    Calculates the NTest
    of the Models: GAModel, RandomModel
    """
    gaModel = model.loadModelFromFile('../Zona/modelo' + str(year) + '.txt')
    modeloReal = model.loadModelFromFile('../Zona/real' + str(year) + '.txt')

    unskilledModel = model.newModel(modeloReal.definitions)
    randomModel.makeRandomModel(unskilledModel)
    unskilledModel.bins = calcNumberBins(unskilledModel.bins, modeloReal.bins)

    gaNTestValue = log.calcNTest(gaModel, modeloReal)
    unskilledNTestValue = log.calcNTest(unskilledModel, modeloReal)

    print(galTestValue)
    print(unskilledlTestValue)


def execLogLikelihood(year):
    """
    Shows the loglikelihood 
    of the Models: GAModel, RandomModel
    """
    gaModel = model.loadModelFromFile('../Zona/modelo' + str(year) + '.txt')
    modeloReal = model.loadModelFromFile('../Zona/real' + str(year) + '.txt')

    unskilledModel = model.newModel(modeloReal.definitions)
    randomModel.makeRandomModel(unskilledModel)
    unskilledModel.bins = calcNumberBins(unskilledModel.bins, modeloReal.bins)

    galLLValue = log.calcLogLikelihood(gaModel, modeloReal)
    unskilledLLValue = log.calcLogLikelihood(unskilledModel, modeloReal)

    print(galLLValue)
    print(unskilledLLValue)


def execTestsbyYear(start=2000, end=2011):
    while(start <= end):
        execGamblingScore(year)
        execAss(year)
        execLTest(year)
        execNTest(year)
        execLogLikelihood(start)
        start += 1
