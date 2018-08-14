CC=mpicc

all: memcpyTest mancpy

memcpyTest: memcpyTest.c inlinememcpy.o
	$(CC) -o memcpyTest -O3 inlinememcpy.o memcpyTest.c

inlinememcpy.o: inlinememcpy.c
	$(CC) -c inlinememcpy.c

mancpy: mancpy.c inlinememcpy.o
	$(CC) -o mancpy -O3 inlinememcpy.o mancpy.c

clean:
	rm *.o
