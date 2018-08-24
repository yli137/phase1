for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./1hintT0 $i $i >> 1hintT0.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./2hintT0 $i $i >> 2hintT0.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./3hintT0 $i $i >> 3hintT0.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./4hintT0 $i $i >> 4hintT0.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./5hintT0 $i $i >> 5hintT0.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./6hintT0 $i $i >> 6hintT0.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./7hintT0 $i $i >> 7hintT0.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./8hintT0 $i $i >> 8hintT0.txt;
done

