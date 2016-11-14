import re

def clear(filename):
	text = open(filename+".txt", 'r')
	saveFile = open(filename+"_R.txt", 'w')

	for line in text:
		data = re.sub(r'avg.*', '', line, flags=re.MULTILINE)		
		saveFile.write(data)
		saveFile.write('\n')

	print("End :D")

	saveFile.close()
	text.close()
