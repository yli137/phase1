for num in {1..8..1}
do
	for i in {40000..560000..40000}
	do
		mpirun -n 1 ./upp_hint $(($i * $num)) $(($i * 8)) $num 8 >> hintdataT0.txt
	done
done
