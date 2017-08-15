for i in {2..25} 
do
	for j in {0..40} 
	do
		# ga  tournsize _ exec_number . txt
		nohup python2.7 benchmarks/benchmarks-gamodelF19.py -i_tournsize 2 -params  'benchmarks/gaParams.txt' -f_tournsize $i &> 'f19_f_tournsize_'$i'.txt' &
		nohup python2.7 benchmarks/benchmarks-gamodelF20.py -i_tournsize 2 -params  'benchmarks/gaParams.txt' -f_tournsize $i &> 'f20_f_tournsize_'$i'.txt' &
		nohup python2.7 benchmarks/benchmarks-gamodelF21.py -i_tournsize 2 -params  'benchmarks/gaParams.txt' -f_tournsize $i &> 'f21_f_tournsize_'$i'.txt' &
		wait
	done
	
done