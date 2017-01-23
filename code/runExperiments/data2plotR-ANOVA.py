import numpy as np


def converter2leastBest(type, region, depth, year_begin, year_end):
    """
    Convert the data form the models: 'listaGA_New', 'gaModel', 'clustered_listaGA_new','clusteredII_listaGA_new', 'clustered_gaModel', 'clusteredII_gaModel'
    """
    year = year_begin
    while(year <= year_end):

        data = list()
        for i in range(10):
            filename = "../Zona2/" + type + '/' + region + "_" + \
                str(depth) + "_" + str(year) + str(i) + ".txtloglikelihood.txt"
            f = open(filename, "r")
            for line in f:
                info = line.split()
                data.append(float(info[0]))
            f.close()

        filename = "../Zona2/dataForR/" + type + "_" + \
            region + "_" + str(depth) + "_" + str(year) + ".txt"
        with open(filename, 'w') as f:
            for i in range(10):
                f.write(str(data[i]))
                f.write("\n")
        year += 1


def converter2leastBestHybrid(type, region, depth, year_begin, year_end):
    """
    Convert the data from the hybrid models 
    """
    year = year_begin
    while(year <= year_end):
        data = list()
        for i in range(10):
            filename = "../Zona2/" + type + '/' + type + region + "_" + \
                str(depth) + "_" + str(year) + '_' + \
                str(i) + ".txtloglikelihood.txt"
            f = open(filename, "r")
            for line in f:
                info = line.split()
                data.append(float(info[0]))
            f.close()

        filename = "../Zona2/dataForR/" + type + "_" + \
            region + "_" + str(depth) + "_" + str(year) + ".txt"
        with open(filename, 'w') as f:
            for i in range(10):
                f.write(str(data[i]))
                f.write("\n")
        year += 1



def converter2leastSC(type, region, depth, year_begin, year_end):
    """
    Convert the data from the models composed with the SC catalog
    """
    file = type.split('_')
    year = year_begin
    while(year <= year_end):

        data = list()
        for i in range(10):
            if type == 'gaModel':
                filename = '../Zona3/scModel/gamodel' + region + '_' + \
                    str(depth) + '_' + str(year) + \
                    str(i) + '.txtloglikelihood.txt'
            elif region == 'EastJapan':
                filename = '../Zona3/scModel/eastgamodel' + region + '_' + \
                    str(depth) + '_' + str(year) + \
                    str(i) + '.txtloglikelihood.txt'
            else:
                filename = '../Zona3/scModel/listgamodel' + region + '_' + \
                    str(depth) + '_' + str(year) + \
                    str(i) + '.txtloglikelihood.txt'
            f = open(filename, "r")
            for line in f:
                info = line.split()
                data.append(float(info[0]))
            f.close()

        filename = "../Zona2/dataForR/SC" + type + "_" + \
            region + "_" + str(depth) + "_" + str(year) + ".txt"
        with open(filename, 'w') as f:
            for i in range(10):
                f.write(str(data[i]))
                f.write("\n")
        year += 1



def main():
    """
    This calls functions to transform data to be easily access the log-lilihood in R
    """
    types = ('listaGA_New', 'gaModel', 'clustered_listaGA_new','clusteredII_listaGA_new', 'clustered_gaModel', 'clusteredII_gaModel')
    regions = ('EastJapan', 'Kanto', 'Kansai', 'Tohoku')
    depth = 100

    for region in regions:
        converter2leastBestHybrid('hybrid_gaModel', region, depth, 2005, 2010)
        converter2leastBestHybrid('hybrid_ListaGA_New', region, depth, 2005, 2010)
        converter2leastSC('gaModel', region, depth, 2005, 2010)
        converter2leastSC('ListaGA_New', region, depth, 2005, 2010)
        converter2leastSC('sc_hybrid_ListaGA_New', region, depth, 2005, 2010)
        converter2leastSC('sc_hybrid_gaModel', region, depth, 2005, 2010)
        for t in types:
          converter2leastBest(t, region, depth, 2005, 2010)


if __name__ == "__main__":
    main()