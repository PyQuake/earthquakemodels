for i in {3..25} 
do
	for j in {0..40} 
	do
		# ga  tournsize _ exec_number . txt
		nohup python2.7 benchmarks/benchmarks-gamodelF1.py -i_tournsize 2 -params  'benchmarks/gaParams.txt' -f_tournsize $i &> 'f1_f_tournsize_'$i'.txt' &
		nohup python2.7 benchmarks/benchmarks-gamodelF2.py -i_tournsize 2 -params  'benchmarks/gaParams.txt' -f_tournsize $i &> 'f2_f_tournsize_'$i'.txt' &
		nohup python2.7 benchmarks/benchmarks-gamodelF3.py -i_tournsize 2 -params  'benchmarks/gaParams.txt' -f_tournsize $i &> 'f3_f_tournsize_'$i'.txt' &
		wait		
	done
	
done