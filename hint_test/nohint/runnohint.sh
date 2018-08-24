for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./1nohintT0 $i $i >> 1nohintT0.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./2nohintT0 $i $i >> 2nohintT0.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./3nohintT0 $i $i >> 3nohintT0.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./4nohintT0 $i $i >> 4nohintT0.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./5nohintT0 $i $i >> 5nohintT0.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./6nohintT0 $i $i >> 6nohintT0.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./7nohintT0 $i $i >> 7nohintT0.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./8nohintT0 $i $i >> 8nohintT0.txt;
done

