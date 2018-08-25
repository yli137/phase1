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

#define NPC 1
#define stride 8
void do_upp(const int OUTPUTSIZE, const int INPUTSIZE){
	MPI_Datatype ddt;
	MPI_Type_vector( OUTPUTSIZE, NPC, stride, MPI_DOUBLE, &ddt );
	MPI_Type_commit(&ddt);

	double *inbuf = (double*)malloc(sizeof(double) * INPUTSIZE);
	double *packed = (double*)malloc(sizeof(double) * OUTPUTSIZE);
	double *obuf = (double*)malloc(sizeof(double) * INPUTSIZE);

	//initialize
	unsigned int i;
	for(i = 0; i < INPUTSIZE; i++)
		inbuf[i] = (double)(rand() % 200);
	for(i = 0; i < INPUTSIZE; i++)
		obuf[i] = (double)(rand() % 200);

	double st, et;
	int position = 0;
	MPI_Pack(inbuf, 1, ddt, packed, OUTPUTSIZE, &position, MPI_COMM_WORLD);

	print_r(inbuf, INPUTSIZE, "inbuf");
	print_r(packed, OUTPUTSIZE, "packed");
	print_r(obuf, INPUTSIZE, "obuf");
	

	MPI_Type_free(&ddt);
	free(inbuf);
	free(packed);
	free(obuf);
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
