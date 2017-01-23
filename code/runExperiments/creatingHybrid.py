import csep.loglikelihood
import gaModel.etasGaModelNP as etasGaModelNP
import models.model as model
import models.modelEtasGa as etasGa

#TODO: probaby this will need not to save but to return a model. So I may remove the saving code part and use only a year

def execCreatingHybridSCwithGAModel(region, depth, year_begin, year_end):
    """
    Create a hybrid between the GAModel + SC with the equations from ETAS + Ideas from RI
    It saves the hybrid in: ./code/Zona2/sc_hybrid_gaModel/hybrid_gaModel"+region +'_' +str(depth) +'_' +str(year) +'_' +str(i) +".txt"
    year_begin is the year from where to start creating the hybrid
    year_end is the year from where to end creating the hybrid
    """
    year = year_begin
    while(year <= year_end):
        # loading comparative real data
        for i in range(10):
            # loading the gaModel to be hybrid(ed)...
            model_ = etasGa.loadModelFromFile(
                '../Zona3/scModel/gamodel' +
                region +
                '_' +
                str(depth) +
                '_' +
                str(year) +
                str(i) +
                '.txt')
            # loading mag file...
            fileEtasim = "../Zona/paper_exp/etasim1.txt"
            # creating hybrid
            modelL = etasGa.sumTriggeredByDaysWithRI(model_, year, fileEtasim)
            # calculating loglike...
            model_ = model.loadModelFromFile(
                '../Zona2/realData/' + region + 'real' + "_" + str(year) + '.txt')
            modelL.loglikelihood = csep.loglikelihood.calcLogLikelihood(
                modelL, model_)
            # saving the hybrid
            etasGa.saveModelToFile(
                modelL,
                "../Zona2/sc_hybrid_gaModel/hybrid_gaModel" +
                region +
                '_' +
                str(depth) +
                '_' +
                str(year) +
                '_' +
                str(i) +
                ".txt")

        year += 1

def execCreatingHybridSCwithListModel(region, depth, year_begin, year_end):
    """
    Create a hybrid between the List Model + SC with the equations from ETAS + Ideas from RI
    It saves the hybrid in: ./code/Zona2/sc_hybrid_ListaGA_New/hybrid_ListaGA_New" + region + '_' + str(depth) + '_' + str(year) + '_' + str(i) +".txt"
    year_begin is the year from where to start creating the hybrid
    year_end is the year from where to end creating the hybrid
    """
    year = year_begin
    while(year <= year_end):
        # loading comparative real data
        for i in range(10):
            # loading the list model to be hybrid(ed)...
            if region == 'EastJapan':
                model_ = etasGa.loadModelFromFile(
                    '../Zona3/scModel/eastgamodel' +
                    region +
                    '_' +
                    str(depth) +
                    '_' +
                    str(year) +
                    str(i) +
                    '.txt')
            else:
                model_ = etasGa.loadModelFromFile(
                    '../Zona3/scModel/listgamodel' +
                    region +
                    '_' +
                    str(depth) +
                    '_' +
                    str(year) +
                    str(i) +
                    '.txt')
            # loading mag file...
            fileEtasim = "../Zona/paper_exp/etasim1.txt"
            # creating hybrid
            modelL = etasGa.sumTriggeredByDaysWithRI(model_, year, fileEtasim)
            # calculating loglike...
            model_ = model.loadModelFromFile(
                '../Zona2/realData/' + region + 'real' + "_" + str(year) + '.txt')
            modelL.loglikelihood = csep.loglikelihood.calcLogLikelihood(
                modelL, model_)
            # saving the hybrid
            etasGa.saveModelToFile(
                modelL,
                "../Zona2/sc_hybrid_ListaGA_New/hybrid_ListaGA_New" +
                region +
                '_' +
                str(depth) +
                '_' +
                str(year) +
                '_' +
                str(i) +
                ".txt")
        year += 1
            


def main():
    """
    Calls the functions to create hybrids.
    It calls the functions for regions: EastJpan, Kanto, Kansai, Tohoku
    From years 2005 to 2010
    """
    regions = ('EastJapan', 'Kanto', 'Kansai', 'Tohoku')
    depth = 100
    for region in regions:
        # the year here already is the target year
        execCreatingHybridSCwithGAModel(region, depth, 2005, 2010)
        execCreatingHybridSCwithListModel(region, depth, 2005, 2010)


if __name__ == "__main__":
    main()
