for i in {2..25} 
do
	# repetition loop
	for j in {0..40} 
	do
		nohup python2.7 benchmarks-pseudo-adaptative/benchmarks-gamodelF17.py -tournsize "$i" -params  'benchmarks-pseudo-adaptative/gaParams.txt' &
		nohup python2.7 benchmarks-pseudo-adaptative/benchmarks-gamodelF18.py -tournsize "$i" -params  'benchmarks-pseudo-adaptative/gaParams.txt' &
		nohup python2.7 benchmarks-pseudo-adaptative/benchmarks-gamodelF19.py -tournsize "$i" -params  'benchmarks-pseudo-adaptative/gaParams.txt' &
		nohup python2.7 benchmarks-pseudo-adaptative/benchmarks-gamodelF20.py -tournsize "$i" -params  'benchmarks-pseudo-adaptative/gaParams.txt' &
wait
	done
done