CC=mpicc

all: v1 nov1 maxBand

v1: hintv1.c v1.o
	$(CC) -o v1 v1.o -O3 hintv1.c

v1.o: v1.c
	$(CC) -c v1.c

nov1: nohint.c nov1.o
	$(CC) -o nov1 nov1.o -O3 nohint.c

nov1.o: nov1.c
	$(CC) -c nov1.c

maxBand: max.c mv1.o
	$(CC) -o maxBand mv1.o -O3 max.c

mv1.o: mv1.c
	$(CC) -c mv1.c

clean:
	rm *.o
