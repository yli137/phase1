#include<mpi.h>
#include<stdio.h>
#include<stdlib.h>

void print_r(const double *input, const int size, const char *name){
	unsigned int i;
	printf("%s: ", name);
	for( i = 0; i < size; i++ )
		printf("%.f ", input[i]);
	printf("\n");
}

double *packBuffer(const int size){
	double *buf = (double*)malloc(sizeof(double) * size);
	unsigned int i;
	for(i = 0; i < size; i++)
		buf[i] = (double)(rand() % 200);
	return buf;
}

int main(int argc, char **argv){
	int procid, num_procs;

	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &procid);
	MPI_Comm_size(MPI_COMM_WORLD, &num_procs);

	MPI_Datatype ddt;
	MPI_Type_vector( 1, atoi(argv[1]), atoi(argv[1]), MPI_DOUBLE, &ddt );
	MPI_Type_commit(&ddt);

	if(procid == 0){
		double *inbuf = packBuffer( atoi(argv[1]) );
		double st, et;

		st = MPI_Wtime();
		MPI_Send(inbuf, 1, ddt, 1, 0, MPI_COMM_WORLD  );
		et = MPI_Wtime();

		printf("size: %d send: %.7f\n", 
			sizeof(double) * atoi(argv[1]),
			sizeof(double) * atoi(argv[1]) / ( (et - st) * 1000000000 ) );

		free(inbuf);
	} else if(procid == 1){
		
		double *obuf = (double*)malloc(sizeof(double) * atoi(argv[1]));

		MPI_Recv(obuf, 1, ddt, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

		free(obuf);
	} else {
		MPI_Finalize();
		MPI_Type_free(&ddt);
		exit(0);
	}

	MPI_Type_free(&ddt);
	MPI_Finalize();
	exit(0);
}
