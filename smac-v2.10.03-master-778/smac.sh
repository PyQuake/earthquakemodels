#!/bin/bash
pip install git+https://github.com/DEAP/deap
pip install numpy
pip install pymysql
./smac --scenario-file algorithm/gaTest-scenario.txt 
