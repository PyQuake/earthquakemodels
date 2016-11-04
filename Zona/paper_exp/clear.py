import re

def cleaner(filename, save):

	text = open(filename, 'r')
	saveFile = open(save, 'w')
	print("entrou")
	for line in text:
		data = re.sub(r'".*" ', '', line, flags=re.MULTILINE)		
		data = re.sub(r'".*"', '', data, flags=re.MULTILINE)		
		saveFile.write(data)
		saveFile.write('\n')

	saveFile.close()
	text.close()

	print("End :D")

def main():
	region="EastJapan"
	print(region)
	year=2006
	while(year<=2010):
		filename='./MediaModelo'+region+'_'+str(year)+'.txt'
		save='./MediaModelo'+region+'_'+str(year)+'cleaned.txt'
		cleaner(filename,save)
		year+=1
	region="Kanto"
	print(region)
	year=2006
	while(year<=2010):
		filename='./MediaModelo'+region+'_'+str(year)+'.txt'
		save='./MediaModelo'+region+'_'+str(year)+'cleaned.txt'
		cleaner(filename,save)
		year+=1
	region="Kansai"
	print(region)
	year=2006
	while(year<=2010):
		filename='./MediaModelo'+region+'_'+str(year)+'.txt'
		save='./MediaModelo'+region+'_'+str(year)+'cleaned.txt'
		cleaner(filename,save)
		year+=1
	region="Tohoku"
	print(region)
	year=2006
	while(year<=2010):
		filename='./MediaModelo'+region+'_'+str(year)+'.txt'
		save='./MediaModelo'+region+'_'+str(year)+'cleaned.txt'
		cleaner(filename,save)
		year+=1
	region="EastJapan"
	print(region)
	year=2006
	while(year<=2010):
		filename='./MediaNP'+region+'_'+str(year)+'.txt'
		save='./MediaNP'+region+'_'+str(year)+'cleaned.txt'
		cleaner(filename,save)
		year+=1
	region="Kanto"
	print(region)
	year=2006
	while(year<=2010):
		filename='./MediaNP'+region+'_'+str(year)+'.txt'
		save='./MediaNP'+region+'_'+str(year)+'cleaned.txt'
		cleaner(filename,save)
		year+=1
	region="Kansai"
	print(region)
	year=2006
	while(year<=2010):
		filename='./MediaNP'+region+'_'+str(year)+'.txt'
		save='./MediaNP'+region+'_'+str(year)+'cleaned.txt'
		cleaner(filename,save)
		year+=1
	region="Tohoku"
	print(region)
	year=2006
	while(year<=2010):
		filename='./MediaNP'+region+'_'+str(year)+'.txt'
		save='./MediaNP'+region+'_'+str(year)+'cleaned.txt'
		cleaner(filename,save)
		year+=1

if __name__ == "__main__":
	main()
