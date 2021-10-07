# Conway's Game of Life

## About
The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. It is Turing complete and can simulate a universal constructor or any other Turing machine. 

The game is played on a two-dimensional rectangular grid of cells. Each cell can be either alive or dead. The status of each cell changes each turn of the game (also called a generation) depending on the statuses of that cell's 8 neighbors. Neighbors of a cell are cells that touch that cell, either horizontal, vertical, or diagonal from that cell.

The initial pattern is the first generation. The second generation evolves from applying the rules simultaneously to every cell on the game board, i.e. births and deaths happen simultaneously. Afterwards, the rules are iteratively applied to create future generations. For each generation of the game, a cell's status in the next generation is determined by a set of rules.

### Rules
1. If the cell is alive, then it stays alive if it has either 2 or 3 live neighbors
2. If the cell is dead, then it springs to life only in the case that it has exactly 3 live neighbors
3. All other cells die or remain dead

## More details:    
You can find more details about Conway's Game of Life at [cornell.edu](http://pi.math.cornell.edu/~lipa/mec/lesson6.html) and [Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

## Features:
- choose the grid size for playing
- the program randomly fills the initial configuration of cells

## Instructions:
1. Clone the repo
2. Run the program with `python3 conways.py`