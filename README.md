# earthquakemodels

GitHub code source:

https://github.com/PyQuake/earthquakemodels

Here is the code for generating Earthquake Risk Models using Genetic Algorithms. 

# Some Background

Some information outside the project frenquently used can be found at:
  
  http://www.corssa.org/articles/themevi/zechar
  
  http://www.cseptesting.org/
  
  https://github.com/stat157/background/issues/26
  
  http://www.jstor.org/stable/3085650?seq=2#page_scan_tab_contents

List of packages
-------------
The project uses the programming language Python, version 3.X.X. 
The python libraries used are:
sys
math
array
numpy
datetime
time
random
deap 
pymysql
multiprocessing
mysql (and, sql)

Getting Started
---------------


# Get the latest version
To get the last version you should clone the repository from gitHub to your local files.
```bash
git clone https://github.com/PyQuake/earthquakemodels.git

# How is the code organized
Most of the code were develop to be run in a python3 interpreter. 
You may find that some files can be bash executed.

The most important files are divided into three types of files: [1] the Genetic Algorithm (GA) files that create earthquake risk models, [2] the files that are the base to the GA files and [3] the files that connect them.

The files in [1] can be found, mostly, at ./code/gaModel.
The files in [2] can be found, mostly, at ./code/csep or ./code/earthquake
The files in [3] can be found, mostly, at ./code/models

It is possible to use the code that I used in most of my experiments. They are located at ./code/runExperiments
# Executing the main GA methods 
```bash
First you need to install all packages and download the source code from GitHub.

Then you may need run the following sql script to save/load models


SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema earthquakemodelsDB
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema earthquakemodelsDB
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `earthquakemodelsDB` ;
USE `earthquakemodelsDB` ;

-- -----------------------------------------------------
-- Table `earthquakemodelsDB`.`earthquakeModels`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `earthquakemodelsDB`.`earthquakeModels` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `modelName` TEXT NULL,
  `bins` TEXT NULL,
  `year` TEXT NULL,
  `loglikelihood` TEXT NULL,
  `definitions` TEXT NULL,
  `logbook` TEXT NULL,
  `time` TEXT NULL,
  `probability` TEXT NULL,
  `executionNumber` TEXT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

After running it and solving all dependencies, you may run a script in ./code/runExperiments

For example (assuming that your working directory is ./code/):

  python3 runExperiments/applyGaModel.py 

To see the models results and analyse, it is possible to load them and/or retrieve them with some functions that are in ./code/model, mainly:

  ./code/model/model.showModelsDB
  ./code/model/model.removeModelDB
  ./code/model/model.loadModelDB
```
