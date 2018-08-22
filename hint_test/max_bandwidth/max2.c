#include<mpi.h>
#include<stdio.h>
#include<stdlib.h>

void do_test(const int OUTPUTSIZE, const int INPUTSIZE){
	unsigned int rep;
	double avg = 0;

	for(rep = 0; rep < 21; rep++){
		double *inbuf = (double*)malloc(sizeof(double) * INPUTSIZE);
		unsigned int i, j;
		for( i = 0; i < INPUTSIZE; i++)
			inbuf[i] = (double)(rand() % 200);
		double *packed = (double*)malloc(sizeof(double) * OUTPUTSIZE);

		double st, et;
		st = MPI_Wtime();

		j = 0;
		for( i = 0; i+2 < OUTPUTSIZE && j+2 < INPUTSIZE ; i+=2){
			packed[i] = inbuf[j];
			packed[i+1] = inbuf[j+1];
			j+=2;
		}

		et = MPI_Wtime();

		if(rep != 0)
			avg += et - st;
		free(inbuf);
		free(packed);
	}

	avg /= 20.;
	printf("OUTPUTSIZE: %d INPUTSIZE: %d Bandwidth: %.7f GBps\n", 
			OUTPUTSIZE, INPUTSIZE, 
			(double)(OUTPUTSIZE * sizeof(double)) / (avg * 1000000000.)  );
}

int main(int argc, char **argv){
	int procid, num_procs;

	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &procid);
	MPI_Comm_size(MPI_COMM_WORLD, &num_procs);

	if(procid != 0){
		MPI_Finalize();
		exit(0);
	}

	do_test( atoi(argv[1]), atoi(argv[2]) );

	MPI_Finalize();
	exit(0);
}
