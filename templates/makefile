CC=mpicc

all: v1

v1: hintv1.c v1.o
	$(CC) -o v1 v1.o -O3 hintv1.c

v1.o: v1.c
	$(CC) -c v1.c

clean:
	rm *.o
