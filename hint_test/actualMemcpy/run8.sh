for i in {40000..540000..40000};
do
        mpirun -np 20 ./8nohintT0 $(($i*8)) $(($i*8)) >> memcpy8_redo.txt;
done
