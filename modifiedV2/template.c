#include<stdio.h>
#include<stdlib.h>
#include<mpi.h>

void do_work(const int OUTPUTSIZE, const int INPUTSIZE, const int stride){

}

int main(int argc, char **argv){
	int rank, size;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);

	if(rank != 0){
		MPI_Finalize();
		exit(0);
	}

	if(argc < 4){
		printf("Not enough for input\n");
		exit(0);
	}

	do_work( atoi(argv[1]), atoi(argv[2]), atoi(argv[3]) );

	MPI_Finalize();
	exit(0);
}
