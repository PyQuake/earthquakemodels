# k loop
for i in {2..25} 
do
	# repetition loop
	for j in {0..40} 
	do
		python2.7 benchmarks/benchmarks-gamodelF1.py -params 'benchmarks/gaParams.txt' -i_tournsize $i -f_tournsize $i 
		python2.7 benchmarks/benchmarks-gamodelF2.py -params 'benchmarks/gaParams.txt' -i_tournsize $i -f_tournsize $i 
		python2.7 benchmarks/benchmarks-gamodelF3.py -params 'benchmarks/gaParams.txt' -i_tournsize $i -f_tournsize $i 
		python2.7 benchmarks/benchmarks-gamodelF4.py -params 'benchmarks/gaParams.txt' -i_tournsize $i -f_tournsize $i 
		python2.7 benchmarks/benchmarks-gamodelF5.py -params 'benchmarks/gaParams.txt' -i_tournsize $i -f_tournsize $i 
		 python2.7 benchmarks/benchmarks-gamodelF6.py -params 'benchmarks/gaParams.txt' -i_tournsize $i -f_tournsize $i 
		 python2.7 benchmarks/benchmarks-gamodelF7.py -params 'benchmarks/gaParams.txt' -i_tournsize $i -f_tournsize $i 
		 python2.7 benchmarks/benchmarks-gamodelF8.py -params 'benchmarks/gaParams.txt' -i_tournsize $i -f_tournsize $i 
		 python2.7 benchmarks/benchmarks-gamodelF9.py -params 'benchmarks/gaParams.txt' -i_tournsize $i -f_tournsize $i 
		 python2.7 benchmarks/benchmarks-gamodelF10.py -params 'benchmarks/gaParams.txt' -i_tournsize $i -f_tournsize $i 
		 python2.7 benchmarks/benchmarks-gamodelF11.py -params 'benchmarks/gaParams.txt' -i_tournsize $i -f_tournsize $i 
		 python2.7 benchmarks/benchmarks-gamodelF12.py -params 'benchmarks/gaParams.txt' -i_tournsize $i -f_tournsize $i 
		 python2.7 benchmarks/benchmarks-gamodelF13.py -params 'benchmarks/gaParams.txt' -i_tournsize $i -f_tournsize $i 
		 python2.7 benchmarks/benchmarks-gamodelF14.py -params 'benchmarks/gaParams.txt' -i_tournsize $i -f_tournsize $i 
		 python2.7 benchmarks/benchmarks-gamodelF15.py -params 'benchmarks/gaParams.txt' -i_tournsize $i -f_tournsize $i 
		 python2.7 benchmarks/benchmarks-gamodelF16.py -params 'benchmarks/gaParams.txt' -i_tournsize $i -f_tournsize $i 
		 python2.7 benchmarks/benchmarks-gamodelF17.py -params 'benchmarks/gaParams.txt' -i_tournsize $i -f_tournsize $i 
		 python2.7 benchmarks/benchmarks-gamodelF18.py -params 'benchmarks/gaParams.txt' -i_tournsize $i -f_tournsize $i 
		 python2.7 benchmarks/benchmarks-gamodelF19.py -params 'benchmarks/gaParams.txt' -i_tournsize $i -f_tournsize $i 
		 python2.7 benchmarks/benchmarks-gamodelF20.py -params 'benchmarks/gaParams.txt' -i_tournsize $i -f_tournsize $i 
		 python2.7 benchmarks/benchmarks-gamodelF21.py -params 'benchmarks/gaParams.txt' -i_tournsize $i -f_tournsize $i 
		 python2.7 benchmarks/benchmarks-gamodelF22.py -params 'benchmarks/gaParams.txt' -i_tournsize $i -f_tournsize $i 
		 python2.7 benchmarks/benchmarks-gamodelF23.py -params 'benchmarks/gaParams.txt' -i_tournsize $i -f_tournsize $i 
		 python2.7 benchmarks/benchmarks-gamodelF24.py -params 'benchmarks/gaParams.txt' -i_tournsize $i -f_tournsize $i 
		wait
	done
done