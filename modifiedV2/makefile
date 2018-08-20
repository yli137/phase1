CC=mpicc

all: memcpyTest mancpy

memcpyTest: memcpyTest.c inlinememcpy.o
	$(CC) -o memcpyTest inlinememcpy.o memcpyTest.c

inlinememcpy.o: inlinememcpy.c
	$(CC) -c inlinememcpy.c

mancpy: mancpy.c inlinememcpy.o
	$(CC) -o mancpy inlinememcpy.o mancpy.c

clean:
	rm *.o
