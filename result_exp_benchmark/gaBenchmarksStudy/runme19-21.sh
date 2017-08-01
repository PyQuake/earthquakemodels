
for i in {2..25} 
do
	for j in {0..40} 
	do
		# ga  tournsize _ exec_number . txt
		nohup python2.7 benchmarks/benchmarks-gamodelF19.py -tournsize "$i" -params  'benchmarks/gaParams.txt' &> 'f19_'$i'_'$j'.txt' &
		nohup python2.7 benchmarks/benchmarks-gamodelF20.py -tournsize "$i" -params  'benchmarks/gaParams.txt' &> 'f20_'$i'_'$j'.txt' &
		nohup python2.7 benchmarks/benchmarks-gamodelF21.py -tournsize "$i" -params  'benchmarks/gaParams.txt' &> 'f21_'$i'_'$j'.txt' &
		wait
	done
	
done