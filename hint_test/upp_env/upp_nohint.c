#include<mpi.h>
#include<stdio.h>
#include<stdlib.h>

void print_r(const double *input, const int size, const char *name){
	printf("%s\n", name);
	unsigned int i;
	for(i = 0; i < size; i++)
		printf("%.f ", input[i]);
	printf("\n");
}

void do_upp(const int OUTPUTSIZE, const int INPUTSIZE){
	
}

int main(int argc, char **argv){
	int procid, num_procs;

	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &procid);
	MPI_Comm_size(MPI_COMM_WORLD, &num_procs);

	if( procid != 0 ){
		MPI_Finalize();
		exit(0);
	}

	do_upp( atoi(argv[1]), atoi(argv[2]) );

	MPI_Finalize();
	exit(0);
}
