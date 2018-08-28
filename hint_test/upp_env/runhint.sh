for num in {1..8..1}
do
	for i in {4000..560000..4000}
	do
		mpirun -n 1 ./upp_hint $(($i * $num)) $(($i * 8)) $num 8 >> hintdata.txt
	done
done
