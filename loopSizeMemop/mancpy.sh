for j in {8..64..8};
do
	for i in {10000..1200000..4000};
	do
		mpirun -n 2 ./op $i $(($i * 8)) 8 >> manualcpy_test.txt;
	done
done
