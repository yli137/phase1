#include<stdio.h>
#include<stdlib.h>
#include<mpi.h>
#include "inlinememcpy.h"

#define CACHE_FLUSH_SIZE 36000
void do_work(const int OUTPUTSIZE, const int INPUTSIZE, const int stride, const int perCache){
	if( (perCache * (INPUTSIZE / stride)) > INPUTSIZE ){
		printf("input sizes not matching\n");
		return;
	}

	double avg = 0;
	unsigned int rep = 0;

	for( rep = 0; rep < 21; rep++){
		double *inbuf = (double*)malloc(sizeof(double) * INPUTSIZE);
		double *obuf = (double*)malloc(sizeof(double) * OUTPUTSIZE);

		unsigned int i, j, z;
		double st, et;
		//initialize input buffer
		for( i = 0; i < INPUTSIZE; i++)
			inbuf[i] = (double)(rand() % 200);

		st = MPI_Wtime();
		j = 0;
		z = 0;
		for( i = 0; i < INPUTSIZE; i+=stride){
			for(z = 0; z < perCache; z++){
				obuf[j] = inbuf[i+z];
				j++;
			}
		}
		et = MPI_Wtime();

		if(rep != 0)
			avg += et - st;

		//print_array(inbuf, INPUTSIZE, "input");
		//print_array(obuf, OUTPUTSIZE, "output");

		double *flush_cache = (double*)malloc(sizeof(double) * CACHE_FLUSH_SIZE);
		for( i = 0; i < CACHE_FLUSH_SIZE; i++)
			flush_cache[i] = (double)(rand() % 200);

		free(inbuf);
		free(obuf);
		free(flush_cache);
	}

	avg /= 20.;
	printf("OUTPUTSIZE: %d INPUTSIZE: %d perCache: %d bandwidth: %.7f GBps\n", 
		OUTPUTSIZE, INPUTSIZE, perCache, (double)(OUTPUTSIZE * sizeof(double)) / (avg * 1000000000) );

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

	do_work( atoi(argv[1]), atoi(argv[2]), atoi(argv[3]), atoi(argv[4]) );

	MPI_Finalize();
	exit(0);
}
