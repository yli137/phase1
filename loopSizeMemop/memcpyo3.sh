for j in {8..64..8};
do
	for i in {10000..1200000..4000}; 
	do
		mpirun -n 2 ../memop_o3/memop $i $(($i * 8)) 8 >> memcpy_testO3.txt;
	done
done

