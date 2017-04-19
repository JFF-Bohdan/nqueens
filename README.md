# nqueens.py
Calculates count of solutions for N-Queen problem.


## General information

Main idea of N-Queen problem is to place 

**N-Queen problem** - you need N chess queens on a chess board with dimensions NxN in a way that they do not
threat each other (according to chess rules). 

Program can find all possible solutions for N-dimensional board. Also, program able to print available solutions to console or to the file.

## Usage

### Command line keys

```
Options:
  -h, --help            show this help message and exit
  -d DIMENSIONS, --dimensions=DIMENSIONS
                        Dimensions for chess board
  -p, --printsolutions  Prints solutions
```

### Usage


#### With solutions on the screen

Calculate solution for 4 dimension board and print to console:

```bash
$ nqueens.py -p -d 4
```

You will got something like this:

```
2017-04-18 20:46:20,629 - DEBUG - solver initialized for chessboard size: 4
2017-04-18 20:46:20,630 - INFO - solution:
_ _ Q _
Q _ _ _
_ _ _ Q
_ Q _ _
2017-04-18 20:46:20,633 - INFO - solution:
_ Q _ _
_ _ _ Q
Q _ _ _
_ _ Q _
2017-04-18 20:46:20,635 - INFO - solutions search complete, found solutions coun
t: 2
2017-04-18 20:46:20,636 - INFO - total solutions count - 2
2017-04-18 20:46:20,637 - INFO - done at 0.01s
Done
```

Where:

```
_ _ Q _
Q _ _ _
_ _ _ Q
_ Q _ _
```

one of possible solutions.


#### Calculating solutions count

When you need just count solutions count, you can execute `nqueens` using:

```bash
$ nqueens.py -d 8
```

You will get someting like this

```
2017-04-18 20:47:49,566 - DEBUG - solver initialized for chessboard size: 8
2017-04-18 20:47:49,605 - INFO - solutions search complete, found solutions coun
t: 92
2017-04-18 20:47:49,606 - INFO - total solutions count - 92
2017-04-18 20:47:49,607 - INFO - done at 0.04s
```

So, total solutions count for 8-dimensional board is **92**.