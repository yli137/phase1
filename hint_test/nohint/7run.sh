for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./7nohintT0 $(($i*7)) $(($i*8)) >> 7nohintT0.txt;
done


for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./8nohintT0 $(($i*8)) $(($i*8)) >> 8nohintT0.txt;
done

