#include<mpi.h>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<xmmintrin.h>

void print_r(const double *input, const int size, const char *name){
	unsigned int i;
	printf("%s\n", name);
	for(i = 0; i < size; i++)
		printf("%.f ", input[i]);
	printf("\n");
}

inline void _memcpy(void *dest, const void *src, size_t n){
	memcpy(dest, src, n);
}

void do_memcpy(const int OUTPUTSIZE, const int INPUTSIZE){
	unsigned int rep;
	double avg = 0;

	for(rep = 0; rep < 21; rep++){
		double *inbuf = (double*)malloc(sizeof(double) * INPUTSIZE);
		unsigned int i, j;
		for( i = 0; i < INPUTSIZE; i++ )
			inbuf[i] = (double)(rand() % 200);
		double *packed = (double*)malloc(sizeof(double) * OUTPUTSIZE);
		double st, et;

		st = MPI_Wtime();
		j = 0; i = 0;
		_mm_prefetch(&inbuf[j], _MM_HINT_T1);
		for( ; i < OUTPUTSIZE && j < INPUTSIZE; i+=7){
			if( j+8 < INPUTSIZE )
				_mm_prefetch(&inbuf[j+8], _MM_HINT_T1);
			_memcpy(&packed[i], &inbuf[j], sizeof(double));
			_memcpy(&packed[i+1], &inbuf[j+1], sizeof(double));
			_memcpy(&packed[i+2], &inbuf[j+2], sizeof(double));
			_memcpy(&packed[i+3], &inbuf[j+3], sizeof(double));
			_memcpy(&packed[i+4], &inbuf[j+4], sizeof(double));
			_memcpy(&packed[i+5], &inbuf[j+5], sizeof(double));
			_memcpy(&packed[i+6], &inbuf[j+6], sizeof(double));
			j+=8;
		}
		et = MPI_Wtime();

		if(rep != 0)
			avg += et - st;
		free(inbuf);
		free(packed);
	}

	avg/=20.;
	printf("%d %d %.7f GBps\n",
			OUTPUTSIZE, INPUTSIZE,
			(double)(OUTPUTSIZE * sizeof(double))/(avg * 1000000000)
	      );
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

	do_memcpy(atoi(argv[1]), atoi(argv[2]) );

	MPI_Finalize();
	exit(0);
}
