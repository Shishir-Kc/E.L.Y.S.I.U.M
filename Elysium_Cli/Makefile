CC = gcc
SRC =  main.c $(wildcard commands/*/*.c) $(wildcard internal/*/*.c)
OUT = test
CFAGS =-I.

build:
	$(CC) $(CFAGS) $(SRC) -o $(OUT)

clean:
	rm -rf $(OUT)
	clear
