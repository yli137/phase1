for i in {10000..1200000..4000}; 
do
	mpirun -n 2 ./memop $i $(($i * 8)) 8 >> memcpy_test.txt;
	mpirun -n 2 ./op $i $(($i * 8)) 8 >> manualcpy_test.txt;
	mpirun -n 2 ./oppref $i $(($i * 8)) 8 >> manualcpy_wprefetch.txt;
done
