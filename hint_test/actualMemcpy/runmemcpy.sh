for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./1nohintT0 $i $(($i*8)) >> memcpy1.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./2nohintT0 $(($i*2)) $(($i*8)) >> memcpy2.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./3nohintT0 $(($i*3)) $(($i*8)) >> memcpy3.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./4nohintT0 $(($i*4)) $(($i*8)) >> memcpy4.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./5nohintT0 $(($i*5)) $(($i*8)) >> memcpy5.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./6nohintT0 $(($i*6)) $(($i*8)) >> memcpy6.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./7nohintT0 $(($i*7)) $(($i*8)) >> memcpy7.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./8nohintT0 $(($i*8)) $(($i*8)) >> memcpy8.txt;
done

