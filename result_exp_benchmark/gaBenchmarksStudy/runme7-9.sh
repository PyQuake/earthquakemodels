for i in {2..25} 
do
	for j in {0..40} 
	do
		# ga  tournsize _ exec_number . txt
		nohup python2.7 benchmarks/benchmarks-gamodelF7.py -i_tournsize 2 -params  'benchmarks/gaParams.txt' -f_tournsize $i &> 'f7_f_tournsize_'$i'.txt' &
		nohup python2.7 benchmarks/benchmarks-gamodelF8.py -i_tournsize 2 -params  'benchmarks/gaParams.txt' -f_tournsize $i &> 'f8_f_tournsize_'$i'.txt' &
		nohup python2.7 benchmarks/benchmarks-gamodelF9.py -i_tournsize 2 -params  'benchmarks/gaParams.txt' -f_tournsize $i &> 'f9_f_tournsize_'$i'.txt' &
		wait
		
	done
	
done