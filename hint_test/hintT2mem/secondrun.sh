for i in {40000..540000..40000}; 
do
	mpirun -np 1 ./1hintT0 $i $(($i*8)) >> 1hintT2_2.txt;
done

for i in {40000..540000..40000}; 
do
	mpirun -np 1 ./2hintT0 $(($i*2)) $(($i*8)) >> 2hintT2_2.txt;
done

for i in {40000..540000..40000}; 
do
	mpirun -np 1 ./3hintT0 $(($i*3)) $(($i*8)) >> 3hintT2_2.txt;
done

for i in {40000..540000..40000}; 
do
	mpirun -np 1 ./4hintT0 $(($i*4)) $(($i*8)) >> 4hintT2_2.txt;
done

for i in {40000..540000..40000}; 
do
	mpirun -np 1 ./5hintT0 $(($i*5)) $(($i*8)) >> 5hintT2_2.txt;
done

for i in {40000..540000..40000}; 
do
	mpirun -np 1 ./6hintT0 $(($i*6)) $(($i*8)) >> 6hintT2_2.txt;
done

for i in {40000..540000..40000}; 
do
	mpirun -np 1 ./7hintT0 $(($i*7)) $(($i*8)) >> 7hintT2_2.txt;
done

for i in {40000..540000..40000}; 
do
	mpirun -np 1 ./8hintT0 $(($i*8)) $(($i*8)) >> 8hintT2_2.txt;
done

