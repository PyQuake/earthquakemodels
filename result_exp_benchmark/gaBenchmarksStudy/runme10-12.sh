<<<<<<< HEAD

=======
>>>>>>> 0ea4363f13d9859ddc41218174c4e6beb8222c9b
for i in {3..25} 
do
	# for j in {3..40} 
	# do
		# ga  tournsize _ exec_number . txt
<<<<<<< HEAD
		nohup python2.7 benchmarks/benchmarks-gamodelF10.py -i_tournsize 2 f_tournsize "$j" -params  'benchmarks-pseudo-adaptative/gaParams.txt' &
		nohup python2.7 benchmarks/benchmarks-gamodelF11.py -i_tournsize 2 f_tournsize "$j" -params  'benchmarks-pseudo-adaptative/gaParams.txt' &
		nohup python2.7 benchmarks/benchmarks-gamodelF12.py -i_tournsize 2 f_tournsize "$j" -params  'benchmarks-pseudo-adaptative/gaParams.txt' &
=======
		nohup python2.7 benchmarks/benchmarks-gamodelF10.py -i_tournsize 2 -params  'benchmarks/gaParams.txt' -f_tournsize $i &
		nohup python2.7 benchmarks/benchmarks-gamodelF11.py -i_tournsize 2 -params  'benchmarks/gaParams.txt' -f_tournsize $i &
		nohup python2.7 benchmarks/benchmarks-gamodelF12.py -i_tournsize 2 -params  'benchmarks/gaParams.txt' -f_tournsize $i &
>>>>>>> 0ea4363f13d9859ddc41218174c4e6beb8222c9b
		wait
	# done
	
done