import models.model as model


def createCSEPmodels():
    year = 2000
    while(year < 2011):
        gaModel = model.loadModelFromFile(
            '../Zona/modelo' + str(year) + '.txt', withMag=False)
        # modeloReal=model.loadModelFromFile('../Zona/real'+str(year)+'.txt')
        print("Converting the models from this framework to the miniCSEP temaplate...")
        model.modelToMiniCSEP(gaModel,
                              "../experiments/gaModel" + str(year),
                              str(year),
                              str(year + 1))
        year += 1
