#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include "v1.h"

void do_memcpy(const int OUTPUTSIZE, const int INPUTSIZE, const int stride, const int NPC){
	double *inbuf = (double*)malloc(sizeof(double) * INPUTSIZE);
	unsigned int i;
	for(i = 0; i < INPUTSIZE; i++)
		inbuf[i] = (double)(rand());
	double *packed = (double*)malloc(sizeof(double) * OUTPUTSIZE);



	free(inbuf);
	free(packed);
}

void inline inlinememcpy(void *dest, const void *src, size_t len){
	memcpy(dest, src, len);
}
