for i in {2..25} 
do
	# repetition loop
	for j in {0..40} 
	do
		nohup python2.7 benchmarks-pseudo-adaptative/benchmarks-gamodelF9.py -tournsize "$i" -params 'benchmarks-pseudo-adaptative/gaParams.txt' & 
		nohup python2.7 benchmarks-pseudo-adaptative/benchmarks-gamodelF10.py -tournsize "$i" -params 'benchmarks-pseudo-adaptative/gaParams.txt' &
		nohup python2.7 benchmarks-pseudo-adaptative/benchmarks-gamodelF11.py -tournsize "$i" -params 'benchmarks-pseudo-adaptative/gaParams.txt' &
		nohup python2.7 benchmarks-pseudo-adaptative/benchmarks-gamodelF12.py -tournsize "$i" -params 'benchmarks-pseudo-adaptative/gaParams.txt' &
		wait
	done
done