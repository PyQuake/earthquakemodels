
for i in {25..25} 
do
	for j in {0..36..4} 
	do
		# ga  tournsize _ exec_number . txt
		num=$(($j + 0))
		nohup python2.7 algorithm/gamodel_bbob.py -tournsize "$i" -year '2006' -params  'algorithm/gaParams.txt' -region 'EastJapan' &> 'ga_'$i'_'$num'.txt' &
        num=$(($j + 1))
		nohup python2.7 algorithm/gamodel_bbob.py -tournsize "$i" -year '2006' -params  'algorithm/gaParams.txt' -region 'EastJapan' &> 'ga_'$i'_'$num'.txt' &
        num=$(($j + 2))
		nohup python2.7 algorithm/gamodel_bbob.py -tournsize "$i" -year '2006' -params  'algorithm/gaParams.txt' -region 'EastJapan' &> 'ga_'$i'_'$num'.txt' &
        num=$(($j + 3))
		nohup python2.7 algorithm/gamodel_bbob.py -tournsize "$i" -year '2006' -params  'algorithm/gaParams.txt' -region 'EastJapan' &> 'ga_'$i'_'$num'.txt' &
	wait
	done
done

