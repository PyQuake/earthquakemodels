
for i in {3..25} 
do
	# for j in {0..40} 
	# do
	# 	# ga  tournsize _ exec_number . txt
		nohup python2.7 benchmarks/benchmarks-gamodelF7.py -i_tournsize 2 f_tournsize "$j" -params  'benchmarks-pseudo-adaptative/gaParams.txt' &
		nohup python2.7 benchmarks/benchmarks-gamodelF8.py -i_tournsize 2 f_tournsize "$j" -params  'benchmarks-pseudo-adaptative/gaParams.txt' &
		nohup python2.7 benchmarks/benchmarks-gamodelF9.py -i_tournsize 2 f_tournsize "$j" -params  'benchmarks-pseudo-adaptative/gaParams.txt' &
		wait
		
	# done
	
done