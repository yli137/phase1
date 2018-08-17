for i in {1000..800000..1000};
do
	mpirun -np 20 ./mancpy $(($i * 3)) $(($i * 8)) 8 3 >> mancpyTesting3.txt
done
