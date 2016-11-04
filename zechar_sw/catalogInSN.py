def catalogInSN(filename, new_filename):

	f = open(filename,"r")
	ret = list()

	for line in f:
	    variables = line.split()
	    
	    lon = variables[0]
	    lat = variables[1]
	    
	    lon = float(lon)
	    lat = float(lat)

	    lon_SN="{:.16e}".format(lon)
	    lat_SN="{:.16e}".format(lat)

	    f = open(new_filename,"a")
	    f.write(str(lon_SN))
	    f.write("	  ")
	    f.write(str(lat_SN))
	    f.write("	   ")
	    f.close()