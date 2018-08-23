for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./nov1 $i $i >> nohint3_max_bandwidth.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./v1 $i $i >> hintT0_max_bandwidth.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./t1 $i $i >> hintT1_max_bandwidth.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./t2 $i $i >> hintT2_max_bandwidth.txt;
done

