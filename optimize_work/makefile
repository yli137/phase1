CC=mpicc

all: memop op oppref

memop: memop.c
	$(CC) -o memop memop.c

op: op.c
	$(CC) -o op op.c

oppref: op_wpref.c
	$(CC) -o oppref op_wpref.c

clean:
	rm *.o
