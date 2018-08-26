for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./6nohintT0 $(($i*6)) $(($i*8)) >> 6nohintT0.txt;
done


