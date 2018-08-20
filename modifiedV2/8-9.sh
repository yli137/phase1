for i in {1000..800000..1000};
do
	mpirun -np 20 ./mancpy $(($i * 8)) $(($i * 8)) 8 8 >> mancpyTesting8-9.txt
done

