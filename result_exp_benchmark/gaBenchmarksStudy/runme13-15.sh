for i in {2..25} 
do
	for j in {0..40} 
	do
		# ga  tournsize _ exec_number . txt
		nohup python2.7 benchmarks/benchmarks-gamodelF13.py -i_tournsize 2 -params  'benchmarks/gaParams.txt' -f_tournsize $i &> 'f13_f_tournsize_'$i'.txt' &
		nohup python2.7 benchmarks/benchmarks-gamodelF14.py -i_tournsize 2 -params  'benchmarks/gaParams.txt' -f_tournsize $i &> 'f14_f_tournsize_'$i'.txt' &
		nohup python2.7 benchmarks/benchmarks-gamodelF15.py -i_tournsize 2 -params  'benchmarks/gaParams.txt' -f_tournsize $i &> 'f15_f_tournsize_'$i'.txt' &
		wait
	done
	
done