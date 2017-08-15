for i in {2..25} 
do
	for j in {0..40} 
	do
		# ga  tournsize _ exec_number . txt
		nohup python2.7 benchmarks/benchmarks-gamodelF16.py -i_tournsize 2 -params  'benchmarks/gaParams.txt' -f_tournsize $i &> 'f16_f_tournsize_'$i'.txt' &
		nohup python2.7 benchmarks/benchmarks-gamodelF17.py -i_tournsize 2 -params  'benchmarks/gaParams.txt' -f_tournsize $i &> 'f17_f_tournsize_'$i'.txt' &
		nohup python2.7 benchmarks/benchmarks-gamodelF18.py -i_tournsize 2 -params  'benchmarks/gaParams.txt' -f_tournsize $i &> 'f18_f_tournsize_'$i'.txt' &
		wait
	done
	
done