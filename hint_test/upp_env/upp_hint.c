#include<mpi.h>
#include<stdio.h>
#include<stdlib.h>

void print_r(const double *input, const int size, const char *name){
	printf("%s: ", name);
	unsigned int i;
	for(i = 0; i < size; i++)
		printf("%.f ", input[i]);
	printf("\n");
}

void do_upp(const int OUTPUTSIZE, const int INPUTSIZE, const int NUM, const int stride){
	double avg = 0, upavg = 0;
	unsigned int rep = 0;

	for( rep = 0; rep < 21; rep++){
		MPI_Datatype ddt;
		MPI_Type_vector( 1 , NUM, stride, MPI_DOUBLE, &ddt );
		MPI_Type_commit(&ddt);

		double *inbuf = (double*)malloc(sizeof(double) * INPUTSIZE);
		double *packed = (double*)malloc(sizeof(double) * OUTPUTSIZE);

		unsigned int i;
		for(i = 0; i < INPUTSIZE; i++)
			inbuf[i] = (double)(rand() % 200);

		double st, et;
		int position = 0;

		st = MPI_Wtime();
		MPI_Pack(inbuf, (int)(OUTPUTSIZE / NUM), ddt, packed, OUTPUTSIZE * sizeof(double), &position, MPI_COMM_WORLD);
		et = MPI_Wtime();

		if( rep != 0 ){
			avg += et - st;
		}

		MPI_Type_free(&ddt);
		free(inbuf);
		free(packed);

		if(rep == 2)
			break;
	}

	avg /= 20.;
	printf("OUTPUTSIZE: %d INPUTSIZE: %d #/line: %d stride: %d pack_bandwidth: %.7f GBps\n",
		OUTPUTSIZE, INPUTSIZE, NUM, stride, (double)(OUTPUTSIZE * sizeof(double)) / (avg * 1000000000.));

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

	do_upp( atoi(argv[1]), atoi(argv[2]), atoi(argv[3]), atoi(argv[4]) );

	MPI_Finalize();
	exit(0);
}
