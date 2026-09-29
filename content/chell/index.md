# 🐚 chell

_C · POSIX · Linux_

A small Unix shell written in C, built to understand what really happens when you type a command into a terminal: process creation, program replacement, and the parent/child relationship behind every command.

[View on GitHub](https://github.com/travisdotdev/chell)

> 🚧 Work in progress,  currently reads and executes a single command, then exits.

## How it works

Each command goes through four steps:

1. **Read** — `fgets` pulls a line from stdin and the trailing newline is trimmed
2. **Tokenize** — `strtok` splits the line on spaces into a NULL-terminated `argv` array
3. **Fork** — the process duplicates itself, producing a parent and a child
4. **Exec** — the child calls `execvp`, replacing its memory image with the target program, while the parent blocks in `wait` until it finishes

## No shortcuts

The interesting constraint is doing everything with raw POSIX primitives (`fork`, `execvp`, `wait`) rather than calling `system()`, which would just hand the hard parts back to `/bin/sh`.

## Features

- Commands are resolved through `PATH`, so anything installed on your system works
- Arguments are passed straight through to the target program
- Can compile itself

## Running it locally

Requires `gcc` and a POSIX system.

```
git clone https://github.com/travisdotdev/chell.git
cd chell
mkdir -p bin
gcc -Wall -Wextra -Iinclude -o bin/chell main.c src/chell.c
./bin/chell
```

[← Projects](/projects)
