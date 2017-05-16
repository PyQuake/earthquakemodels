python2.7 -c "import math"
if [echo $?]
	then
	echo 'it exists'
fi

cd /root/mpi_projects/earthquakemodels/code/gaModel
python2.7 gamodel_bbob.py teste2 2 Kanto 2000 ../../params/gaParams.txt