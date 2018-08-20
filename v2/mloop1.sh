for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./loopmemcpy $i $i 1 --exclusive >> max_bandwidth.txt;
done

