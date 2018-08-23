for i in {1000..500000..1000}; 
do
	mpirun -np 1 ./max1 $i $i --exclusive >> 1core1double2.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 1 ./max2 $i $i --exclusive >> 1core2double2.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 1 ./max3 $i $i --exclusive >> 1core3double2.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 1 ./max4 $i $i --exclusive >> 1core4double2.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 1 ./max5 $i $i --exclusive >> 1core5double2.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 1 ./max6 $i $i --exclusive >> 1core6double2.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 1 ./max7 $i $i --exclusive >> 1core7double2.txt;
done

for i in {1000..500000..1000}; 
do
	mpirun -np 1 ./max8 $i $i --exclusive >> 1core8double2.txt;
done

for i in {1000..500000..1000};
do
        mpirun -np 20 ./max1 $i $i --exclusive >> 20core1double2.txt;
done

for i in {1000..500000..1000};
do
        mpirun -np 20 ./max2 $i $i --exclusive >> 20core2double2.txt;
done

for i in {1000..500000..1000};
do
        mpirun -np 20 ./max3 $i $i --exclusive >> 20core3double2.txt;
done

for i in {1000..500000..1000};
do
        mpirun -np 20 ./max4 $i $i --exclusive >> 20core4double2.txt;
done

for i in {1000..500000..1000};
do
        mpirun -np 20 ./max5 $i $i --exclusive >> 20core5double2.txt;
done

for i in {1000..500000..1000};
do
        mpirun -np 20 ./max6 $i $i --exclusive >> 20core6double2.txt;
done

for i in {1000..500000..1000};
do
        mpirun -np 20 ./max7 $i $i --exclusive >> 20core7double2.txt;
done

for i in {1000..500000..1000};
do
        mpirun -np 20 ./max8 $i $i --exclusive >> 20core8double2.txt;
done

