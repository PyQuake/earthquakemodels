import urllib2
def readFromFile(filename, outFile):
    """ Returns a catalog created from a JMA or FNET text file
    """
    f = open(filename,"r")
    g = open(outFile,"w")
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
	catalogo=readFromFile('../data/clustered_quakes-M+A.dat', '../data/clustered_quakes-M.dat')

if __name__ == "__main__":
	main()
