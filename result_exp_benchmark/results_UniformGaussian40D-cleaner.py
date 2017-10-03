import os
import re

i = 0
output_file = str()

for file in os.listdir("UniformGaussian40D"):
	if file.endswith(".txt") and file.startswith("f"):

		f = open("UniformGaussian40D/"+file, "r")
		last_file = output_file
		output_file = re.sub ('_[0-9]*.txt', '.txt', file)
		g = open("results_UniformGaussian40D/"+output_file, "a")
		if i < 40:
			for line in f:	
				data = line.split()
				if data[0] != 'gen':
					if len(data) == 5:
						data.append(i)
						output = ', '.join(str(e) for e in data)
						g.write(output)
						g.write('\n')
		if i >= 40 and last_file != output_file:
			i = 0
		else:
			i += 1
		f.close()