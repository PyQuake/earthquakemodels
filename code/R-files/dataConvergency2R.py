import sys
sys.path.insert(0, '..')
import models.model as model
import re

def main():
	modelName='KantoGAModel'
	year=2005
	region = 'Kanto'
	for executionNumber in range(10):
		model_ = model.loadModelDB('KantoGAModel', year, executionNumber)
		with open("dataConvervency4R"+"_"+str(region)+"_"+str(executionNumber)+"_"+str(year), 'w') as f:
			f.write(str(model_.logbook))
			f.write("\n")



if __name__ == "__main__":
    main()
