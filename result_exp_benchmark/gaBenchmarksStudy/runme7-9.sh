

#!/bin/bash
python2.7 -c "import numpy"
if (($? == 1))
then
 echo First you should install numpy by "pip install numpy" 
else
 echo Numpy is already installed. Checking other libraries...
fi

python2.7 -c "import deap"
if (($? == 1))
then
 echo First you should install deap by "pip install git+https://github.com/DEAP/deap"
else
 echo Deap is already installed. Checking other libraries...
fi

python2.7 -c "import pymysql"
if (($? == 1))
then
 echo First you should install pymysql by "pip install pymysql"
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
		nohup python2.7 mpi_projects/earthquakemodels/result_exp_benchmark/gaBenchmarksStudy/benchmarks/benchmarks-gamodelF7.py -tournsize "$i" -params  'mpi_projects/earthquakemodels/result_exp_benchmark/gaBenchmarksStudy/benchmarks/gaParams.txt' &> 'f7_'$i'_'$j'.txt' &
		nohup python2.7 mpi_projects/earthquakemodels/result_exp_benchmark/gaBenchmarksStudy/benchmarks/benchmarks-gamodelF8.py -tournsize "$i" -params  'mpi_projects/earthquakemodels/result_exp_benchmark/gaBenchmarksStudy/benchmarks/gaParams.txt' &> 'f8_'$i'_'$j'.txt' &
		nohup python2.7 mpi_projects/earthquakemodels/result_exp_benchmark/gaBenchmarksStudy/benchmarks/benchmarks-gamodelF9.py -tournsize "$i" -params  'mpi_projects/earthquakemodels/result_exp_benchmark/gaBenchmarksStudy/benchmarks/gaParams.txt' &> 'f9_'$i'_'$j'.txt' &
		wait
		
	done
	
done