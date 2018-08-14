#include<string.h>
#include<stdio.h>
#include "inlinememcpy.h"

inline void inlinememcpy(void *dest, void *src, size_t len){
	memcpy(dest, src, len);
}

void print_array(const double *input, const int size, const char *name){
	unsigned int i;
	printf("%s\n", name);
	for( i = 0; i < size; i++)
		printf("%.f ", input[i]);
	printf("\n");
}
