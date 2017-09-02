import os
import re

i = 0
for file in os.listdir("UniformGaussian40D"):
	if file.endswith(".txt") and file.startswith("f"):
		
		f = open("UniformGaussian40D/"+file, "r")
		if i == 0:
			output_file = re.sub ('_[0-9]*.txt', '.txt', file)
			g = open("results_UniformGaussian40D/"+output_file, "w")
		# f.readline()
		i += 1
		for line in f:
			data = line.split()

			if data[0] == 'gen':
				if i == 0:
					data.append('exp_number')
					output = ', '.join(data)
					g.write(output)
					g.write('\n')
				exp_number = i 
			elif i == 40:
				i = 0
			elif len(data) == 5:
				data.append(exp_number)
				output = ', '.join(str(e) for e in data)
				g.write(output)
				g.write('\n')
		f.close()
	