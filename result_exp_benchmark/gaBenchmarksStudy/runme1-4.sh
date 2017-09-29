# k loop
for i in {2..25} 
do
	# repetition loop
	for j in {0..40} 
	do
		nohup python2.7 benchmarks/benchmarks-gamodelF1.py -params 'benchmarks/gaParams.txt' &
		nohup python2.7 benchmarks/benchmarks-gamodelF2.py -params 'benchmarks/gaParams.txt' &
		nohup python2.7 benchmarks/benchmarks-gamodelF3.py -params 'benchmarks/gaParams.txt' &
		nohup python2.7 benchmarks/benchmarks-gamodelF4.py -params 'benchmarks/gaParams.txt' &
		wait
	done
done