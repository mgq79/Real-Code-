SHELL = /usr/bin/env bash
.PHONY: clean

#Variables
CC = gcc
CCFLAGS = -Wall -Wextra -Werror -std=c99 -pedantic -g

test: stdmeme.h spongeCase.c aestheticCase.c owOofCase.c aggroCase.c l33tCase.c helpers.c test.c memef.c
	$(CC) $(CCFLAGS) helpers.c spongeCase.c aestheticCase.c owOofCase.c aggroCase.c l33tCase.c memef.c test.c -o test

lib: stdmeme.h spongeCase.c aestheticCase.c owOofCase.c aggroCase.c l33tCase.c helpers.c test.c memef.c
	echo "Implement later"

clean:
	rm test
