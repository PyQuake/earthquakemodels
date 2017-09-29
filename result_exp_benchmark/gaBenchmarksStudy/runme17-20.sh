# k loop
for i in {2..25} 
do
	# repetition loop
	for j in {0..40} 
	do
		nohup python2.7 benchmarks/benchmarks-gamodelF17.py -tournsize "$i" -params  'benchmarks/gaParams.txt' &
		nohup python2.7 benchmarks/benchmarks-gamodelF18.py -tournsize "$i" -params  'benchmarks/gaParams.txt' &
		nohup python2.7 benchmarks/benchmarks-gamodelF19.py -tournsize "$i" -params  'benchmarks/gaParams.txt' &
		nohup python2.7 benchmarks/benchmarks-gamodelF20.py -tournsize "$i" -params  'benchmarks/gaParams.txt' &
		wait
	done
done