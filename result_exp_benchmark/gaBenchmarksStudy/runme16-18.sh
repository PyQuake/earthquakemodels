for i in {3..25} 
do
	# for j in {0..40} 
	# do
		# ga  tournsize _ exec_number . txt
		nohup python2.7 benchmarks-pseudo-adaptative/benchmarks-gamodelF16.py -i_tournsize 2 f_tournsize "$i" -params  'benchmarks-pseudo-adaptative/gaParams.txt' &
		nohup python2.7 benchmarks-pseudo-adaptative/benchmarks-gamodelF17.py -i_tournsize 2 f_tournsize "$i" -params  'benchmarks-pseudo-adaptative/gaParams.txt' &
		nohup python2.7 benchmarks-pseudo-adaptative/benchmarks-gamodelF18.py -i_tournsize 2 f_tournsize "$i" -params  'benchmarks-pseudo-adaptative/gaParams.txt' &
		wait
	# done
	
done