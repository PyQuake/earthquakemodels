import os
i = 0
for file in os.listdir("pseudo-adaptative"):
	if file.endswith(".txt") and file.startswith("f"):
		f = open("pseudo-adaptative/"+file, "r")
		g = open("results_pseudo-adaptative/"+file, "a")
		i = 0

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
# i = 0
# output_file = str()

# for file in os.listdir("UniformGaussian10D"):
# 	if file.endswith(".txt") and file.startswith("f"):

# 		f = open("UniformGaussian10D/"+file, "r")
# 		last_file = output_file
# 		output_file = re.sub ('_[0-9]*.txt', '.txt', file)
# 		g = open("results_UniformGaussian10D/"+output_file, "a")
# 		if i < 40:
# 			for line in f:	
# 				data = line.split()
# 				if data[0] != 'gen':
# 					if len(data) == 5:
# 						data.append(i)
# 						output = ', '.join(str(e) for e in data)
# 						g.write(output)
# 						g.write('\n')
# 		if i >= 40 and last_file != output_file:
# 			i = 0
# 		else:
# 			i += 1
# 		f.close()