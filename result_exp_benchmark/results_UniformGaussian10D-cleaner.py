import os
import re

j = 0
i = 0
for file in os.listdir("UniformGaussian10D"):
	if file.endswith(".txt") and file.startswith("f"):

		f = open("UniformGaussian10D/"+file, "r")
		if j == 0:
			output_file = re.sub ('_[0-9]*.txt', '.txt', file)
			g = open("results_UniformGaussian10D/"+output_file, "w")
		# f.readline()
		j += 1

		for line in f:
			data = line.split()

			if data[0] == 'gen':
				exp_number = i 
			elif i == 40:
				i = 0
				j = 0
				break
			elif len(data) == 5:
				data.append(i)
				output = ', '.join(str(e) for e in data)
				g.write(output)
				g.write('\n')
		i+=1	
		f.close()