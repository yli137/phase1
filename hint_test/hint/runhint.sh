for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./nov1 $i $i >> nohint_max_bandwidth.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./v1 $i $i >> hint_max_bandwidth.txt;
done

