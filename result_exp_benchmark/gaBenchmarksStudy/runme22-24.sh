for i in {2..25} 
do
	for j in {0..40} 
	do
		# ga  tournsize _ exec_number . txt
		nohup python2.7 benchmarks/benchmarks-gamodelF22.py -i_tournsize 2 -params  'benchmarks/gaParams.txt' -f_tournsize $i &> 'f22_f_tournsize_'$i'.txt' &
		nohup python2.7 benchmarks/benchmarks-gamodelF23.py -i_tournsize 2 -params  'benchmarks/gaParams.txt' -f_tournsize $i &> 'f23_f_tournsize_'$i'.txt' &
		nohup python2.7 benchmarks/benchmarks-gamodelF24.py -i_tournsize 2 -params  'benchmarks/gaParams.txt' -f_tournsize $i &> 'f24_f_tournsize_'$i'.txt' &
	wait
	done
	
done