CC=mpicc

all: memcpyTest mancpy loopmemcpy

memcpyTest: memcpyTest.c inlinememcpy.o
	$(CC) -o memcpyTest -O3 inlinememcpy.o memcpyTest.c

inlinememcpy.o: inlinememcpy.c
	$(CC) -c inlinememcpy.c

mancpy: mancpy.c inlinememcpy.o
	$(CC) -o mancpy -O3 inlinememcpy.o mancpy.c

loopmemcpy: loopmemcpy.c inlinememcpy.o
	$(CC) -o loopmemcpy -O3 inlinememcpy.o loopmemcpy.c

clean:
	rm *.o
