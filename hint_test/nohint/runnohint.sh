for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./1nohintT0 $i $(($i*8)) >> 1nohintT0.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./2nohintT0 $(($i*2)) $(($i*8)) >> 2nohintT0.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./3nohintT0 $(($i*3)) $(($i*8)) >> 3nohintT0.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./4nohintT0 $(($i*4)) $(($i*8)) >> 4nohintT0.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./5nohintT0 $(($i*5)) $(($i*8)) >> 5nohintT0.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./6nohintT0 $(($i*6)) $(($i*8)) >> 6nohintT0.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./7nohintT0 $(($i*7)) $(($i*8)) >> 7nohintT0.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./8nohintT0 $(($i*8)) $(($i*8)) >> 8nohintT0.txt;
done

