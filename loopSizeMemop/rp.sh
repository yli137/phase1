for j in {8..64..8};
do
	for i in {10000..1200000..4000}; 
	do
		mpirun -n 2 ./memop $i $(($i * $j)) $j >> memcpy_test.txt;
	done
done


for j in {8..64..8};
do
	for i in {10000..1200000..4000};
	do
		mpirun -n 2 ./op $i $(($i * 8)) 8 >> manualcpy_test.txt;
	done
done

for j in {8..64..8};
do
	for i in {10000..1200000..4000};
	do
		mpirun -n 2 ./oppref $i $(($i * 8)) 8 >> manualcpy_wprefetch.txt;
	done
done

for j in {8..64..8};
do
	for i in {10000..1200000..4000}; 
	do
		mpirun -n 2 ../memop_o3/memop $i $(($i * 8)) 8 >> memcpy_testO3.txt;
	done
done

for j in {8..64..8};
do
	for i in {10000..1200000..4000};
	do
		mpirun -n 2 ../memop_o3/op $i $(($i * 8)) 8 >> manualcpy_testO3.txt;
	done
done

for j in {8..64..8};
do
	for i in {10000..1200000..4000};
	do
		mpirun -n 2 ../memop_o3/oppref $i $(($i * 8)) 8 >> manualcpy_wprefetchO3.txt;
	done
done
