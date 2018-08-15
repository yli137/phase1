for i in {1000..800000..1000}; 
do
	mpirun -np 20 ./mancpy $i $i 1 --exclusive >> max_bandwidth_manual.txt;
done

for j in {1..8..1};
do
	for i in {1000..800000..1000};
	do
		mpirun -np 20 ./mancpy $i $($i * 8) $j >> mancpyTesting.txt
	done
done
