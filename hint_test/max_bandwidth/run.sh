for i in {1000..500000..1000}; 
do
	mpirun -np 1 ./max1 $i $i --exclusive >> 1cmax1.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 1 ./max2 $i $i --exclusive >> 1cmax2.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 1 ./max3 $i $i --exclusive >> 1cmax3.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 1 ./max4 $i $i --exclusive >> 1cmax4.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 1 ./max5 $i $i --exclusive >> 1cmax5.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 1 ./max6 $i $i --exclusive >> 1cmax6.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 1 ./max7 $i $i --exclusive >> 1cmax7.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 1 ./max8 $i $i --exclusive >> 1cmax8.txt;
done

