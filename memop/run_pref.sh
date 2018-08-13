for i in {10000..1200000..4000};
do
	mpirun -n 2 ../memop_o3/oppref $i $(($i * 8)) 8 >> manualcpy_wprefetchO3.txt;
done
