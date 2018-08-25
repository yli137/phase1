for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./1nohintT0 $i $i >> memcpy1.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./2nohintT0 $i $i >> memcpy2.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./3nohintT0 $i $i >> memcpy3.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./4nohintT0 $i $i >> memcpy4.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./5nohintT0 $i $i >> memcpy5.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./6nohintT0 $i $i >> memcpy6.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./7nohintT0 $i $i >> memcpy7.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 20 ./8nohintT0 $i $i >> memcpy8.txt;
done

