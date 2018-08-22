for i in {1000..500000..1000}; 
do
	mpirun -np 1 ./max8 $i $i --exclusive >> max8single.txt;
done

