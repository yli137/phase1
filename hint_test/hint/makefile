CC=mpicc

all: v1 nov1 t1 t2

v1: hint.c
	$(CC) -o v1 -O3 hint.c

nov1: nohint.c
	$(CC) -o nov1 -O3 nohint.c

t1: hintt1.c
	$(CC) -o t1 -O3 hintt1.c

t2: hintt2.c
	$(CC) -o t2 -O3 hintt2.c

clean:
	rm *.o
