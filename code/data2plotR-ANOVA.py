import numpy as np

# logbook_gaModelClustered/Tohoku_2011_logbook
# logbook_listaGA_newClustered/EastJapan_2005_logbook


def converter2leastBest(type, region, depth, year_begin, year_end):

    year = year_begin
    while(year <= year_end):
        print(year)
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

    year = year_begin
    while(year <= year_end):
        print(year)
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


def converter2leastBestHybridWindow(type, region, depth, year_begin, year_end):
    file = type.split('_')
    year = year_begin
    while(year <= year_end):
        print(year)
        data = list()
        for i in range(10):
            # hybrid_ListaGA_NewEastJapan_25_2005_0
            if len(file) == 4:  # new
                filename = "../Zona2/" + type + '/' + file[1] + '_' + file[2] + '_' + file[
                    3] + region + "_" + str(depth) + "_" + str(year) + '_' + str(i) + ".txtloglikelihood.txt"
            else:
                filename = "../Zona2/" + type + '/' + file[1] + '_' + file[2] + region + "_" + str(
                    depth) + "_" + str(year) + '_' + str(i) + ".txtloglikelihood.txt"
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


def converter2leastBestHybridSLC(type, region, depth, year_begin, year_end):
    file = type.split('_')
    year = year_begin
    while(year <= year_end):
        print(year)
        data = list()
        for i in range(10):
            # hybrid_ListaGA_NewEastJapan_25_2005_0
            filename = "../Zona2/" + type + '/hybrid_' + file[1] + '_' + file[2] + region + "_" + str(
                depth) + "_" + str(year) + '_' + str(i) + ".txtloglikelihood.txt"
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
    file = type.split('_')
    year = year_begin
    while(year <= year_end):
        print(year)
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
    # types = ('listaGA_New', 'gaModel', 'clustered_listaGA_new','clusteredII_listaGA_new', 'clustered_gaModel', 'clusteredII_gaModel')
    regions = ('EastJapan', 'Kanto', 'Kansai', 'Tohoku')
    depth = 100

    for region in regions:
        print(region)
        # converter2leastBestHybrid('hybrid_gaModel', region, depth, 2005, 2010)
        # converter2leastBestHybrid('hybrid_ListaGA_New', region, depth, 2005, 2010)
        converter2leastSC('gaModel', region, depth, 2005, 2010)
        converter2leastSC('ListaGA_New', region, depth, 2005, 2010)
        converter2leastSC('sc_hybrid_ListaGA_New', region, depth, 2005, 2010)
        converter2leastSC('sc_hybrid_gaModel', region, depth, 2005, 2010)
        # converter2leastBestHybridWindow('clustered_hybrid_gaModel', region, depth, 2005, 2010)
        # converter2leastBestHybridWindow('clustered_hybrid_ListaGA_New', region, depth, 2005, 2010)
        # converter2leastBestHybridWindow('clusteredII_hybrid_gaModel', region, depth, 2005, 2010)
        # converter2leastBestHybridWindow('clusteredII_hybrid_ListaGA_New', region, depth, 2005, 2010)
        # converter2leastBestHybridSLC('clusteredII_hybrid_gaModel', region, depth, 2005, 2010)
        # converter2leastBestHybridSLC('clusteredII_hybrid_ListaGA_New', region, depth, 2005, 2010)
        # for t in types:
        # 	print(t)
        # 	converter2leastBest(t, region, depth, 2005, 2010)


if __name__ == "__main__":
    main()
