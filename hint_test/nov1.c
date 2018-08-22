#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<unistd.h>
#include<mpi.h>
#include "nov1.h"

void print_r(const double *inbuf, const int size, const char *name){
	printf("%s\n", name);
	unsigned int i;
	for(i = 0; i < size; i++){
		printf("%.f ", inbuf[i]);
	}
	printf("\n");
}

inline void phint(void *input){
	asm("PREFETCHT0 %0	\n"
			:
			:"m"(input)
	   );
}

void inline inlinememcpy(void *dest, const void *src, size_t len){
	memcpy(dest, src, len);
}

void do_memcpy(const int OUTPUTSIZE, const int INPUTSIZE, const int stride, const int NPC){
	unsigned int rep;
	double avg = 0;

	for(rep = 0; rep < 21; rep++){
		double *inbuf = (double*)malloc(sizeof(double) * INPUTSIZE);
		unsigned int i, j;
		for(i = 0; i < INPUTSIZE; i++)
			inbuf[i] = (double)(rand() % 15);
		double *packed = (double*)malloc(sizeof(double) * OUTPUTSIZE);

		//PREFETCH_T0(&inbuf[0], 64);
		double et, st;
		j = 0;
		i = 0;
		st = MPI_Wtime();
		//phint(&inbuf[j]);
		for(i = 0; i < INPUTSIZE && j < OUTPUTSIZE; i++){
			packed[i] = inbuf[j];
			j+=stride;
		}
		et = MPI_Wtime();

		if(rep != 0)
			avg += et - st;
		free(inbuf);
		free(packed);
	}

	avg /= 20.;
	printf("OUTPUTSIZE: %d INPUTSIZE: %d perCache: %d bandwidth: %.7f GBps\n",
			OUTPUTSIZE, INPUTSIZE, NPC, (double)(OUTPUTSIZE * sizeof(double)) / (avg * 1000000000.) );
}

