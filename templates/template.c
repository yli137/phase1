#include<mpi.h>
#include<stdio.h>
#include<stdlib.h>

int main(int argc, char **argv){
	int procid, num_procs;
	
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &argc);
	MPI_Comm_size(MPI_COMM_WORLD, &num_procs);

	if(procid != 0){
		MPI_Finalize();
		exit(0);
	}

	MPI_Finalize();
	exit(0);
}
