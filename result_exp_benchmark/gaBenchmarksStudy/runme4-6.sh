
for i in {20..25} 
do
	for j in {0..40} 
	do
		# ga  tournsize _ exec_number . txt
		nohup python2.7 benchmarks/benchmarks-gamodelF4.py -tournsize "$i" -params  'benchmarks/gaParams.txt' &> 'f4_'$i'_'$j'.txt' &
		nohup python2.7 benchmarks/benchmarks-gamodelF5.py -tournsize "$i" -params  'benchmarks/gaParams.txt' &> 'f5_'$i'_'$j'.txt' &
		nohup python2.7 benchmarks/benchmarks-gamodelF6.py -tournsize "$i" -params  'benchmarks/gaParams.txt' &> 'f6_'$i'_'$j'.txt' & 		
		wait
	done
	
done		