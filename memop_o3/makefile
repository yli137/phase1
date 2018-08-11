CC=mpicc

all: memop op oppref

memop: memop.c
	$(CC) -o memop -O3 memop.c

op: op.c
	$(CC) -o op -O3 op.c

oppref: op_wpref.c
	$(CC) -o oppref -O3 op_wpref.c

clean:
	rm *.o
