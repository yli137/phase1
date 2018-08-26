for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./1hintT0 $i $(($i*8)) >> 1hintT1.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./2hintT0 $(($i*2)) $(($i*8)) >> 2hintT1.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./3hintT0 $(($i*3)) $(($i*8)) >> 3hintT1.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./4hintT0 $(($i*4)) $(($i*8)) >> 4hintT1.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./5hintT0 $(($i*5)) $(($i*8)) >> 5hintT1.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./6hintT0 $(($i*6)) $(($i*8)) >> 6hintT1.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./7hintT0 $(($i*7)) $(($i*8)) >> 7hintT1.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./8hintT0 $(($i*8)) $(($i*8)) >> 8hintT1.txt;
done

