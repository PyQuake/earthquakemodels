#!/bin/bash
# nohup python2.7 gamodel_bbob.py output ../../../params/gaParams.txt EastJapan 2006 &
# python2.7 gamodel_bbob.py output ../../../params/gaParams.txt EastJapan 2006
pip2.7 install git+https://github.com/DEAP/deap
pip2.7 install numpy
pip2.7 install pymysql
./smac --scenario-file example_scenarios/branin/gaTest-scenario.txt 

