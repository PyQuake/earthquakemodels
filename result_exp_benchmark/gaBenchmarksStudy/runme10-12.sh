for i in {3..25} 
do
	for j in {0..40} 
	do
		# ga  tournsize _ exec_number . txt
		nohup python2.7 benchmarks/benchmarks-gamodelF10.py -i_tournsize 2 -params  'benchmarks/gaParams.txt' -f_tournsize $i &
		nohup python2.7 benchmarks/benchmarks-gamodelF11.py -i_tournsize 2 -params  'benchmarks/gaParams.txt' -f_tournsize $i &
		nohup python2.7 benchmarks/benchmarks-gamodelF12.py -i_tournsize 2 -params  'benchmarks/gaParams.txt' -f_tournsize $i &
		wait
	done
	
done