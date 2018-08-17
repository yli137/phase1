for j in {1..3..1};
do
	for i in {1000..800000..1000};
	do
		mpirun -np 20 ./mancpy $(($i * $j)) $(($i * 8)) 8 $j >> mancpyTesting1-3.txt
	done
done
