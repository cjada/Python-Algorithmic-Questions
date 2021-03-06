from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9

class Sudoku_UI(Frame):
	"""
	The UI for drawing the board and accepting user input.
	"""
	def __init__(self, parent, game):
		self.game = game
		self.parent = parent
		Frame.__init__(self, parent)

		self.row, self.col = 0, 0

		self.__initUI()

	def __initUI(self):
		self.parent.title("Sudoku Solver")
		self.pack(fill=BOTH, expand=1)
		self.canvas = Canvas(self, width=WIDTH, height=HEIGHT)
		self.canvas.pack(fill=BOTH, side=TOP)
		submit_button = Button(self, text="Submit puzzle", command=self.__submit_puzzle)
		submit_button.pack(fill=BOTH, side=BOTTOM)

		self.__draw_grid()
		self.__draw_puzzle()

		self.canvas.bind("<Button-1>", self.__cell_clicked)
		self.canvas.bind("<Key>", self.__key_pressed)

	def __draw_grid(self):
		"""
		Draw grid divided by blue lines into 3x3 squares
		"""
		for i in range(10):
			color = "blue" if i % 3 == 0 else "gray"

			x0 = MARGIN + i * SIDE 
			y0 = MARGIN
			x1 = MARGIN + i * SIDE 
			y1 = HEIGHT - MARGIN
			self.canvas.create_line(x0, y0, x1, y1, fill=color)

			x0 = MARGIN
			y0 = MARGIN + i * SIDE
			x1 = WIDTH - MARGIN
			y1 = MARGIN + i * SIDE
			self.canvas.create_line(x0, y0, x1, y1, fill=color)

	def  __draw_puzzle(self):
		self.canvas.delete("numbers")
		for i in range(9):
			for j in range(9):
				answer = self.game.puzzle[i][j]				# !!!!
				if answer != 0:
					x = MARGIN + j * SIDE + SIDE / 2
					y = MARGIN + i * SIDE + SIDE / 2
					original = self.game.start_puzzle[i][j]
					color = "black" #if answer == original else "sea green"
					self.canvas.create_text(
						x, y, text=answer, tags="numbers", fill=color
					)

	def __submit_puzzle(self):
		self.game.start(game)
		#self.canvas.delete("victory") // Don't know the effect of this yet
		#self.__draw_puzzle()

	def __cell_clicked(self, event):
		if self.game.game_over:
			return

		x, y = event.x, event.y
		if (MARGIN < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN):
			self.canvas.focus_set()

			row, col = (y - MARGIN) // SIDE, (x - MARGIN) // SIDE

			if (row, col) == (self.row, self.col):
				self.row, self.col = -1, -1
			elif self.game.puzzle[row][col] == 0:
				self.row, self.col = row, col

		self.__draw_cursor()

	def __draw_cursor(self):
		self.canvas.delete("cursor")
		if self.row >= 0 and self.col >= 0:
			x0 = MARGIN + self.col * SIDE + 1
			y0 = MARGIN + self.row * SIDE + 1
			x1 = MARGIN + (self.col + 1) * SIDE - 1
			y1 = MARGIN + (self.row + 1) * SIDE - 1
			self.canvas.create_rectangle(
				x0, y0, x1, y1,
				outline = "red", tags="cursor"
			)

	def __key_pressed(self, event):
		if self.game.game_over:
			return
		if self.row >= 0 and self.col >= 0 and event.char in "1234567890":
			self.game.puzzle[self.row][self.col] = int(event.char)
			self.col, self.row = -1, -1
			self.__draw_puzzle()
			self.__draw_cursor()
			"""
			This is where VICTORY would go.  Maybe include a message
			saying that this problem is solvable (or not)?
			"""






class Sudoku_solver():
	def determineSquare(self, i, j):
		# determine the 3x3 Matrix parameters for any given 9x9 indices
		# Return an array with the 3x3 limits

		x1 = 0
		x2 = 0
		y1 = 0
		y2 = 0

		if j // 3 == 0:
			x2 = 3

		if j // 3 == 1:
			x1 = 3
			x2 = 6

		if j // 3 == 2:
			x1 = 6
			x2 = 9

		if i // 3 == 0:
			y2 = 3

		if i // 3 == 1:
			y1 = 3
			y2 = 6

		if i // 3 == 2:
			y1 = 6
			y2 = 9

		return (x1, x2, y1, y2)

	def isValid(self, arr):
		"""
		Returns True if the sudoku puzzle is solved
		"""
		for i in range(0, 9):
			for j in range(0, 9):
				if arr[i][j] == 0:
					return False
				if not self.isSafe(arr, arr[i][j], i, j):
					return False
		return True
	
	def isSafe(self, arr, num, i, j):
		# Returns True if a number is safe in spot (no conflict with row, column, or 3x3 square)
		# i, j: Int - these are the Sudoku puzzle (S) indices

		# Check columns
		for j1 in range(0, 9):
			if j1 != j and arr[i][j1] == num:
				return False

		# Check rows
		for i1 in range(0, 9):
			if i1 != i and arr[i1][j] == num:
				return False

		# Check 3x3 square
		x1, x2, y1, y2 = self.determineSquare(i, j)
		for i1 in range(y1, y2):
			for j1 in range(x1, x2):
				if j1 != j and i1 != i and arr[i1][j1] == num:
					return False

		return True

	def find_zero(self, arr):
		for i in range(0, 9):
			for j in range(0, 9):
				if arr[i][j] == 0:
					return (i, j)
	
	def solver(self, arr):
		if self.isValid(arr):
			return True

		i, j = self.find_zero(arr)
		for num in range(1, 10):
			if self.isSafe(arr, num, i, j):
				arr[i][j] = num
				if self.solver(arr):
					return (True, arr)
				arr[i][j] = 0
		return False


	def findSolution(self, puzzle):
		solved, puzzle = self.solver(puzzle)
		if solved:
			for l in puzzle:
				print(l)
			print("SOLVED")
			return puzzle
		else:
			print("This cannot be solved")
			return False


class test():
	def generate(self, s):
		s = s.replace(".", "0")
		i = 1
		row = []
		matrix = []
		for digit in s:
			row.append(int(digit))
			if i >= 9:
				matrix.append(row)
				row = []
				i = 0
			i += 1
		return matrix

	"""
	Takes in two string arguments, runs the sudoku solver, and determines whether the solver is correct

	puzzle, answer: string, string (or bool)
	return: bool
	"""
	def evaluate(self, puzzle, answer):
		solver = Sudoku_solver()
		puzzle = self.generate(puzzle)

		if answer != False:
			answer = self.generate(answer)

		return solver.findSolution(puzzle) == answer




if __name__ == '__main__':
	s = "974236158638091742125487936316754289742908563589362417867125394253649871491073625"
	a = "123456789913456789223456789323456789423456879523456789623456789723456789823456789"
	s2 = "3.542.81.4879.15.6.29.5637485.793.416132.8957.74.6528.2413.9.655.867.192.965124.8"
	a2 = "365427819487931526129856374852793641613248957974165283241389765538674192796512438"
	h1 = "..2.3...8.....8....31.2.....6..5.27..1.....5.2.4.6..31....8.6.5.......13..531.4.."
	h2 = "672435198549178362831629547368951274917243856254867931193784625486592713725316489"
	invalid = "...........5....9...4....1.2....3.5....7.....438...2......9.....1.4...6.........."

	t = test()
	print(1, t.evaluate(s, a))
	print(2, t.evaluate(s2, a2))
	print(3, t.evaluate(h1, h2))

	# !!!! This case is failing.  Need to make it quicker.
	print(4, t.evaluate(invalid, False))


	"""
	root = Tk()

	game = Sudoku_solver(c)

	Sudoku_UI(root, Sudoku_solver)
	root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
	root.mainloop()
	"""





















