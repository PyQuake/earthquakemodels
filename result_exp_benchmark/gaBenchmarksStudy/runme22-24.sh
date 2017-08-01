#!/bin/bash
python2.7 -c "import numpy"
if (($? == 1))
then
 echo First you should install numpy by "pip2.7 install numpy" 
else
 echo Numpy is already installed. Checking other libraries...
fi

python2.7 -c "import deap"
if (($? == 1))
then
 echo First you should install deap by "pip2.7 install git+https://github.com/DEAP/deap"
else
 echo Deap is already installed. Checking other libraries...
fi

python2.7 -c "import pymysql"
if (($? == 1))
then
 echo First you should install pymysql by "pip2.7 install pymysql"
else	
 echo Pymysql is already installed. Checking other libraries...
fi

if [ -n 'which java' ]
then
	echo '' 
else 
	echo 'First you should install java 1.7' 
fi


for i in {2..25} 
do
	for j in {0..40} 
	do
		# ga  tournsize _ exec_number . txt
		nohup python2.7 mpi_projects/earthquakemodels/result_exp_benchmark/gaBenchmarksStudy/benchmarks/benchmarks-gamodelF22.py -tournsize "$i" -params  'mpi_projects/earthquakemodels/result_exp_benchmark/gaBenchmarksStudy/benchmarks/gaParams.txt' &> 'f22_'$i'_'$j'.txt' & 
		nohup python2.7 mpi_projects/earthquakemodels/result_exp_benchmark/gaBenchmarksStudy/benchmarks/benchmarks-gamodelF23.py -tournsize "$i" -params  'mpi_projects/earthquakemodels/result_exp_benchmark/gaBenchmarksStudy/benchmarks/gaParams.txt' &> 'f23_'$i'_'$j'.txt' &
		nohup python2.7 mpi_projects/earthquakemodels/result_exp_benchmark/gaBenchmarksStudy/benchmarks/benchmarks-gamodelF24.py -tournsize "$i" -params  'mpi_projects/earthquakemodels/result_exp_benchmark/gaBenchmarksStudy/benchmarks/gaParams.txt' &> 'f24_'$i'_'$j'.txt' &
	wait
	done
	
done