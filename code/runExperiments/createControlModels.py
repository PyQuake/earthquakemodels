import models.randomModel as randomModel
import models.modelEtasGa as etasGa
import models.model as model


def main():

    """
    Create two control models: 1 is a complete Poisson random model and the other is a model with all bins with 1 earthquake
    """

    year = 2005
    while (year <= 2010):
        modelO = etasGa.loadModelFromFile(
            '../Zona/realEtas' + str(year) + '.txt')

        randModel = model.newModel(modelO.definitions, False, 1)
        randModel = randomModel.makePoissonModel(randModel)
        randModel.definitions = modelO.definitions
        randModel.definitions[2]['min'] = 0.0

        tudo1model = model.newModel(modelO.definitions, False, 1)
        tudo1model.definitions = modelO.definitions
        tudo1model.definitions[2]['min'] = 0.0

        etasGa.saveModelToFile(
            randModel, '../Zona/model/teste_RandModel' + str(year) + '.txt')
        etasGa.saveModelToFile(
            tudo1model, '../Zona/model/teste_tudo1model' + str(year) + '.txt')
        year += 1


if __name__ == "__main__":
    main()
