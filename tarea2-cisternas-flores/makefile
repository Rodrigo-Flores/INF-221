CC = g++
CFLAGS = -Wall

all: compile run

input: compile run-input

compile:
	$(CC) $(CFLAGS) main.cpp -o a.out

run:
	./a.out

run-input:
	./a.out < input.dat

clean:
	rm -f a.out
