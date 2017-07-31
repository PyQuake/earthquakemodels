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


for i in {7..10} 
do
	for j in {0..36..4} 
	do
		# ga  tournsize _ exec_number . txt
		num=$(($j + 0))
		nohup python2.7 algorithm/gamodel_bbob.py -tournsize "$i" -year '2006' -params  'algorithm/gaParams.txt' -region 'EastJapan' &> 'ga_'$i'_'$num'.txt' &
        num=$(($j + 1))
		nohup python2.7 algorithm/gamodel_bbob.py -tournsize "$i" -year '2006' -params  'algorithm/gaParams.txt' -region 'EastJapan' &> 'ga_'$i'_'$num'.txt' &
        num=$(($j + 2))
		nohup python2.7 algorithm/gamodel_bbob.py -tournsize "$i" -year '2006' -params  'algorithm/gaParams.txt' -region 'EastJapan' &> 'ga_'$i'_'$num'.txt' &
        num=$(($j + 3))
		nohup python2.7 algorithm/gamodel_bbob.py -tournsize "$i" -year '2006' -params  'algorithm/gaParams.txt' -region 'EastJapan' &> 'ga_'$i'_'$num'.txt' &
	wait
	done
done
