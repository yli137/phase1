for i in {40000..560000..40000}
do
	mpirun -n 1 ./upp_nohint $i $i $i $i >> full2.txt
done
