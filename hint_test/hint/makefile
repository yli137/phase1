CC=mpicc

all: v1 nov1

v1: hint.c
	$(CC) -o v1 -O3 hint.c

nov1: nohint.c
	$(CC) -o nov1 -O3 nohint.c

clean:
	rm *.o
