for j in {3..5..1};
do
	for i in {1000..800000..1000};
	do
		mpirun -np 20 ./mancpy $(($i * $j)) $(($i * 8)) 8 $j >> mancpyTesting3-5.txt
	done
done