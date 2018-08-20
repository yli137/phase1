for i in {1000..800000..1000};
do
	mpirun -np 20 ./mancpy $(($i * 5)) $(($i * 8)) 8 5 >> mancpyTesting5.txt
done
