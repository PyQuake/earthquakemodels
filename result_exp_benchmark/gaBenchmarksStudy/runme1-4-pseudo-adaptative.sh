# k loop
for i in {2..25} 
do
	# repetition loop
	for j in {0..40} 
	do
		nohup python2.7 benchmarks-pseudo-adaptative/benchmarks-gamodelF1.py -tournsize "$i" -params 'benchmarks-pseudo-adaptative/gaParams.txt' &
		nohup python2.7 benchmarks-pseudo-adaptative/benchmarks-gamodelF2.py -tournsize "$i" -params 'benchmarks-pseudo-adaptative/gaParams.txt' &
		nohup python2.7 benchmarks-pseudo-adaptative/benchmarks-gamodelF3.py -tournsize "$i" -params 'benchmarks-pseudo-adaptative/gaParams.txt' &
		nohup python2.7 benchmarks-pseudo-adaptative/benchmarks-gamodelF4.py -tournsize "$i" -params 'benchmarks-pseudo-adaptative/gaParams.txt' &
		wait
	done
done