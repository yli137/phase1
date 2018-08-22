#include<mpi.h>
#include<stdio.h>
#include<stdlib.h>
#include "nov1.h"

int main(int argc, char **argv){
	int procid, num_procs;
	
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &procid);
	MPI_Comm_size(MPI_COMM_WORLD, &num_procs);

	if(procid != 0){
		MPI_Finalize();
		exit(0);
	}

	do_memcpy(atoi(argv[1]), atoi(argv[2]), atoi(argv[3]), atoi(argv[4]));

	MPI_Finalize();
	exit(0);
}
