for i in {1000..500000..1000}; 
do
	mpirun -np 1 ./max1 $i $i --exclusive >> 1core1double.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 1 ./max2 $i $i --exclusive >> 1core2double.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 1 ./max3 $i $i --exclusive >> 1core3double.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 1 ./max4 $i $i --exclusive >> 1core4double.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 1 ./max5 $i $i --exclusive >> 1core5double.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 1 ./max6 $i $i --exclusive >> 1core6double.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 1 ./max7 $i $i --exclusive >> 1core7double.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 1 ./max8 $i $i --exclusive >> 1core8double.txt;
done

for i in {1000..500000..1000};
do
        mpirun -np 20 ./max1 $i $i --exclusive >> 20core1double.txt;
done

for i in {1000..500000..1000};
do
        mpirun -np 20 ./max2 $i $i --exclusive >> 20core2double.txt;
done

for i in {1000..500000..1000};
do
        mpirun -np 20 ./max3 $i $i --exclusive >> 20core3double.txt;
done

for i in {1000..500000..1000};
do
        mpirun -np 20 ./max4 $i $i --exclusive >> 20core4double.txt;
done

for i in {1000..500000..1000};
do
        mpirun -np 20 ./max5 $i $i --exclusive >> 20core5double.txt;
done

for i in {1000..500000..1000};
do
        mpirun -np 20 ./max6 $i $i --exclusive >> 20core6double.txt;
done

for i in {1000..500000..1000};
do
        mpirun -np 20 ./max7 $i $i --exclusive >> 20core7double.txt;
done

for i in {1000..500000..1000};
do
        mpirun -np 20 ./max8 $i $i --exclusive >> 20core8double.txt;
done

