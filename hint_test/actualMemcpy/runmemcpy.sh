for i in {40000..540000..40000}; 
do
	mpirun -np 20 ./1nohintT0 $i $(($i*8)) >> memcpy1_2.txt;
done

for i in {40000..540000..40000}; 
do
	mpirun -np 20 ./2nohintT0 $(($i*2)) $(($i*8)) >> memcpy2_2.txt;
done

for i in {40000..540000..40000}; 
do
	mpirun -np 20 ./3nohintT0 $(($i*3)) $(($i*8)) >> memcpy3_2.txt;
done

for i in {40000..540000..40000}; 
do
	mpirun -np 20 ./4nohintT0 $(($i*4)) $(($i*8)) >> memcpy4_2.txt;
done

for i in {40000..540000..40000}; 
do
	mpirun -np 20 ./5nohintT0 $(($i*5)) $(($i*8)) >> memcpy5_2.txt;
done

for i in {40000..540000..40000}; 
do
	mpirun -np 20 ./6nohintT0 $(($i*6)) $(($i*8)) >> memcpy6_2.txt;
done

for i in {40000..540000..40000}; 
do
	mpirun -np 20 ./7nohintT0 $(($i*7)) $(($i*8)) >> memcpy7_2.txt;
done

for i in {40000..540000..40000}; 
do
	mpirun -np 20 ./8nohintT0 $(($i*8)) $(($i*8)) >> memcpy8_2.txt;
done

