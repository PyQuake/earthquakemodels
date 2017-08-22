for i in {3..25} 
do
	# for j in {0..40} 
	# do
		# ga  tournsize _ exec_number . txt
		nohup python2.7 benchmarks-pseudo-adaptative/benchmarks-gamodelF13.py -i_tournsize 2 -f_tournsize "$i" -params  'benchmarks-pseudo-adaptative/gaParams.txt' &
		nohup python2.7 benchmarks-pseudo-adaptative/benchmarks-gamodelF14.py -i_tournsize 2 -f_tournsize "$i" -params  'benchmarks-pseudo-adaptative/gaParams.txt' &
		nohup python2.7 benchmarks-pseudo-adaptative/benchmarks-gamodelF15.py -i_tournsize 2 -f_tournsize "$i" -params  'benchmarks-pseudo-adaptative/gaParams.txt' &
		wait
	# done
	
done