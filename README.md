# ConwaysGameOfLife
This is a python program I wrote while at PyCon 2017. It was the first Python I wrote and I just wanted to familiarize myself with the basic syntax. This is Conway's Game of Life, a very basic simulation of growing, patterned life. You can find more details about Conway's Game of Life here: https://en.wikipedia.org/wiki/Conway's_Game_of_Life

This is a very basic readme for now. Just explaining how to compile and run, and use the program.
I will use it as a basic update history

# Compile and Run
Use"python Gameoflife.py graphics.py" to compile and run the program

# Using the Program
So far there's not very much to see. Increase the speed field to slow down the simulation, and lower the speed field to speed it up.
Click on a tile to change it's value.
The simulation will run and change the value of of each tile as dictated by the rules of the Game of Life.
A short summary as follows:
  For each tile, determine the number of active neighboring files.
  The value of the current file is as follows:
    0 or 1 active neighbors: the current tile is dead.
    2 active neighbors: the current tile maintains it's current state - whether that's dead or alive.
    3 active neighbors: the current tile is alive.
    4+ active neighbors: the current tile is dead.
    
The best method for setting tile values is to slow the simulation speed to 1000 or more. Once the values are set as you like, lower the speed value to ~10 to see the simulation run.

# Update Log
V0.1 - Initial version. Single file - Basic functionality and simulation speed working.
