# for i in {2..25} 
# do
# 	# repetition loop
# 	for j in {0..40} 
# 	do
		nohup python2.7 benchmarks-pseudo-adaptative/benchmarks-gamodelF13.py -params 'benchmarks-pseudo-adaptative/gaParams.txt' &
		nohup python2.7 benchmarks-pseudo-adaptative/benchmarks-gamodelF14.py -params 'benchmarks-pseudo-adaptative/gaParams.txt' &
		nohup python2.7 benchmarks-pseudo-adaptative/benchmarks-gamodelF15.py -params 'benchmarks-pseudo-adaptative/gaParams.txt' &
		nohup python2.7 benchmarks-pseudo-adaptative/benchmarks-gamodelF16.py -params 'benchmarks-pseudo-adaptative/gaParams.txt' &
# 		wait
# 	done
# done