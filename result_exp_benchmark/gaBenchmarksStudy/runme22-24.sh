# random set.seed
RANDOM=1341
# create middle gen
nohup python2.7 benchmarks-pseudo-adaptative/benchmarks-gamodelF22.py -tournsize 2 -params  'benchmarks-pseudo-adaptative/gaParams.txt' &
nohup python2.7 benchmarks-pseudo-adaptative/benchmarks-gamodelF23.py -tournsize 2 -params  'benchmarks-pseudo-adaptative/gaParams.txt' &
nohup python2.7 benchmarks-pseudo-adaptative/benchmarks-gamodelF24.py -tournsize 2 -params  'benchmarks-pseudo-adaptative/gaParams.txt' & 
wait
# random set.seed
RANDOM=1342
# k loop
for i in {2..25} 
do
	# repetition loop
	for j in {0..40} 
	do
		nohup python2.7 benchmarks-pseudo-adaptative/benchmarks-gamodelF22.py -tournsize "$i" -params  'benchmarks-pseudo-adaptative/gaParams.txt' &
		nohup python2.7 benchmarks-pseudo-adaptative/benchmarks-gamodelF23.py -tournsize "$i" -params  'benchmarks-pseudo-adaptative/gaParams.txt' &
		nohup python2.7 benchmarks-pseudo-adaptative/benchmarks-gamodelF24.py -tournsize "$i" -params  'benchmarks-pseudo-adaptative/gaParams.txt' &
		wait
	done
done