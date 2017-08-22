
for i in {2..25} 
do
	for j in {0..36..4} 
	do
		# ga  tournsize _ exec_number . txt
		num=$(($j + 0))
		python2.7 algorithm/gamodel_bbob.py -tournsize "$i" -year '2006' -params  'algorithm/gaParams.txt' -region 'EastJapan' >> 'ga_'$i'_'$num'.txt'
        num=$(($j + 1))
		python2.7 algorithm/gamodel_bbob.py -tournsize "$i" -year '2006' -params  'algorithm/gaParams.txt' -region 'EastJapan' >> 'ga_'$i'_'$num'.txt'
        num=$(($j + 2))
		python2.7 algorithm/gamodel_bbob.py -tournsize "$i" -year '2006' -params  'algorithm/gaParams.txt' -region 'EastJapan' >> 'ga_'$i'_'$num'.txt'
        num=$(($j + 3))
		python2.7 algorithm/gamodel_bbob.py -tournsize "$i" -year '2006' -params  'algorithm/gaParams.txt' -region 'EastJapan' >> 'ga_'$i'_'$num'.txt'
	done
done