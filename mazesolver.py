from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random


#two finals used, all you have to do is decide the size of the maze
MAZE_SIZE: int = 30
END: int = MAZE_SIZE-1

#our cell for each tile or space in the maze
class Cell(str, Enum):
	EMPTY = "O"
	BLOCKED = "X"
	START = "S"
	GOAL = "G"
	PATH = "*"

#the coordinates of a point in the maze
class MazeLocation(NamedTuple):
	row: int
	column: int

#our main maze class to generate a random maze
class Maze:

	#main initializer
	#Note, the sparseness varible dictates the dificulity of the maze
	#other than that we make the maze our size and place the goal and end
	def __init__(self, rows = MAZE_SIZE, columns= MAZE_SIZE, 
		sparseness= 0.2, start= MazeLocation(0, 0), 
		goal= MazeLocation(END,END)):


		#init basic instance varibles
		self._rows: int = rows
		self._columns: int = columns

		#start and end point coordinates
		self.start: MazeLocation = start
		self.goal: MazeLocation = goal


		#fill the grid with empty cells
		self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]


		#populate the grid with blocked cells
		self._randomly_fill(rows, columns, sparseness)


		#fill the start and goal locations in
		self._grid[start.row][start.column] = Cell.START
		self._grid[goal.row][goal.column] = Cell.GOAL


	# a method to add random blocks in the path
	def _randomly_fill(self, rows, columns, sparseness):
		for row in range(rows):
			for column in range(columns):
				if random.uniform(0, 1.0) < sparseness:
					self._grid[row][column] = Cell.BLOCKED


	#a method for the string to print
	def __str__(self):
		output: str = ""
		for row in self._grid:
			output += " ".join([c.value for c in row]) + "\n" 
		return output


#a completely blank maze that we will fill with the path
class Path:
	def __init__(self, rows = MAZE_SIZE, columns = MAZE_SIZE, 
		start = MazeLocation(0, 0), 
		goal = MazeLocation(END,END)):


		#init basic instance varibles
		self._rows: int = rows
		self._columns: int = columns
		self.start: MazeLocation = start
		self.goal: MazeLocation = goal


		#fill the grid with empty cells
		self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(columns)]
for r in range(rows)]

		#fill the start and goal locations in
		self._grid[start.row][start.column] = Cell.START
		self._grid[goal.row][goal.column] = Cell.GOAL

		#note we never place any blocks in, this is itentional


	# same method to get a string to print
	def __str__(self):
		output: str = ""
		for row in self._grid:
			output += " ".join([c.value for c in row]) + "\n" 
		return output


# make a new maze and print it
maze: Maze = Maze()
print(maze)


#make a new path board
path: Path = Path()

#Our Recursive Function
def findPath(row, col):


	#Check for base case
	if row == END and col == END:

		#save final move 
		path._grid[row][col] = Cell.PATH
		return True


	#the real 'recursion' part
	#if we are in an open tile
	if maze._grid[row][col] == Cell.EMPTY or maze._grid[row][col]== Cell.START:

		#save this current move in our path layout
		path._grid[row][col] = Cell.PATH

		#if we arent at the right edge
		if col<END:

			#call the function again for the square to the right
			if findPath(row, col+1):
				#if the function is true return true again
				return True


		#if we arent at the bottom edge
		if row<END:

			#call the function again for the square beneath it
			if findPath(row+1, col):
				#if the function is true return true again
				return True


		#if we make it this far without breaking out with a return
		#dont save that move
		path._grid[row][col] = Cell.EMPTY

	#return false this maze is impossible or already solved
	return False


findPath(0, 0)
	
for row in range(MAZE_SIZE):
	for col in range(MAZE_SIZE):
		if maze._grid[row][col]== Cell.BLOCKED:
			path._grid[row][col] = Cell.BLOCKED


#find path starting in the top right

#restring our path grid
path.__str__()
#print it
print("\n\n\n SOLVED MAZE:")
print(path)






















































