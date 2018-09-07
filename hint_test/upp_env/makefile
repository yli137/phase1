CC=mpicc

all: upp_nohint upp_hint

upp_hint:
	mpicc -o upp_hint -O3 upp_hint.c -lm

upp_nohint:
	mpicc -o upp_nohint -O3 upp_nohint.c -lm

clean:
	rm upp_hint upp_nohint
