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
		for( i = 0; i+8 < OUTPUTSIZE && j+8 < INPUTSIZE ; i+=8){
			packed[i] = inbuf[j];
			packed[i+1] = inbuf[j+1];
			packed[i+2] = inbuf[j+2];
			packed[i+3] = inbuf[j+3];
			packed[i+4] = inbuf[j+4];
			packed[i+5] = inbuf[j+5];
			packed[i+6] = inbuf[j+6];
			packed[i+7] = inbuf[j+7];
			j+=8;
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
