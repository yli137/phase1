#include<mpi.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void print_r(double *input, int size, char *input_name){
	unsigned int i = 0;
	printf("%s\n", input_name);
	for(; i < size; i++){
		printf("%.f ", input[i]);
	}
	printf("\n");
}

inline void prefetch(void *input){
	__builtin_prefetch(input);
}

#define CACHE_FLUSH_SIZE 36000
void memop(int OUTPUTSIZE, int INPUTSIZE, int stride){
	if(OUTPUTSIZE * stride > INPUTSIZE){
		printf("invalid input sizes\n");
		exit(0);
	}

	unsigned int rep = 0;
	double avg = 0;

	for(rep = 0; rep < 21; rep++){
		double *inbuf = (double*)malloc(sizeof(double) * INPUTSIZE);
		double *packed = (double*)malloc(sizeof(double) * OUTPUTSIZE);

		//initialize inbuf
		unsigned int i;
		for(i = 0; i < INPUTSIZE; i++)
			inbuf[i] = (double)(rand() % 200);

		double st, et; 
		unsigned int j = 0;
		st = MPI_Wtime();
		prefetch(&inbuf[0]);
		prefetch(&packed[j]);
		for(i = 0; i < INPUTSIZE && j < OUTPUTSIZE; i+=stride){
			prefetch(&inbuf[i+stride]);
			prefetch(&packed[j+1]);
			packed[j] = inbuf[i];
			j++;
		}
		packed[j] = inbuf[i];
		et = MPI_Wtime();
		if(rep != 0)
			avg += et - st;

		//print_r(inbuf, INPUTSIZE, "input buffer");
		//print_r(packed, OUTPUTSIZE, "packed buffer");

		double *flush_cache = (double*)malloc(sizeof(double) * CACHE_FLUSH_SIZE);
		for(i = 0; i < CACHE_FLUSH_SIZE; i++)
			flush_cache[i] = (double)(rand() % 200);

		free(flush_cache);
		free(inbuf);
		free(packed);
	}

	avg /= 20.;
	printf("output_size %d input_size %d stride %d bandwidth: %.3f MB/s\n", 
		OUTPUTSIZE, INPUTSIZE, stride, 
		(double)(OUTPUTSIZE * sizeof(double))/(avg * 1000000.));
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

	memop(atoi(argv[1]), atoi(argv[2]), atoi(argv[3]));

	MPI_Finalize();
	exit(0);
}
