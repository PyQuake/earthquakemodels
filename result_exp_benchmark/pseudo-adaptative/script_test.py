import os

for file in os.listdir("."):
	if file.endswith(".txt") and file.startswith("f"):

		f = open(file, "r")
		g = open("../results_pseudo-adaptative/"+file, "w")
		w = open("../targets/target_"+file, "w")
		i = 0
		w.write(f.readline())
		w.close()

		for line in f:
			data = line.split()

			if data[0] == 'gen':
				if i == 0:
					data.append('exp_number')
					output = ', '.join(data)
					g.write(output)
					g.write('\n')
				exp_number = i + 1
				i += 1
			else:
				data.append(exp_number)
				output = ', '.join(str(e) for e in data)
				g.write(output)
				g.write('\n')
		f.close()
		g.close()