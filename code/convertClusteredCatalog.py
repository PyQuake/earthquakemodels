import urllib2


def readFromFileSC(filename, outFile):
    """ Returns a catalog created from a JMA or FNET text file
    """
    f = open(filename, "r")
    g = open(outFile, "a")
    keys = None
    ret = list()

    for line in f:
        if line[0] == '#':
            continue
        tokens = line.split()
        # print(tokens)
        if float(tokens[0]) == 1:
            text = ' '.join(tokens[2:12])
            g.write(text)
            g.write('\n')


def readFromFile(filename, outFile):
    """ Returns a catalog created from a JMA or FNET text file
    """
    f = open(filename, "r")
    g = open(outFile, "w")
    keys = None
    ret = list()

    for line in f:
        if line[0] == '#':
            continue
        tokens = line.split()
        if tokens[10] == 'mainshock':
            text = ' '.join(tokens[0:10])
            g.write(text)
            g.write('\n')


def main():
        # catalogo=readFromFile('../data/clustered_quakes-M+A.dat', '../data/clustered_quakes-M.dat')
    # catalogo=readFromFile('../data/regions_classified.dat', '../data/regions_classified-M.dat')
    year = 2000
    while(year < 2011):
        catalogo = readFromFileSC(
            '../data/results/east' + str(year) + '.txt',
            '../data/SC-catalog.dat')
        catalogo = readFromFileSC(
            '../data/results/kanto' + str(year) + '.txt',
            '../data/SC-catalog.dat')
        catalogo = readFromFileSC(
            '../data/results/sendai' + str(year) + '.txt',
            '../data/SC-catalog.dat')
        catalogo = readFromFileSC(
            '../data/results/Touhoku' + str(year) + '.txt',
            '../data/SC-catalog.dat')
        year += 1

if __name__ == "__main__":
    main()
