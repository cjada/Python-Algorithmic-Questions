from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

class Sudoku_UI(Frame):
	"""
	The UI for drawing the board and accepting user input.
	"""
	def __init__(self, parent, game):
		self.game = game
		self.parent = parent
		Frame.__init__(self, parent)

		self.row, self.column = 0, 0

		self.__initUI()

	def __initUI(self):
		self.parent.title("Sudoku Solver")
		self.pack(fill=BOTH, expand=1)
		self.canvas = Canvas(self, width=WIDTH, height=HEIGHT)
		self.canvas.pack(fill=BOTH, side=TOP)
		clear_button = Button(self, text="Clear answers", command=self.__clear_answers)
		clear_button.pack(fill=BOTH, side=BOTTOM)

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
				answer = self.game.puzzle[i][j]
				if answer != 0:
					x = MARGIN + j * SIDE + SIDE / 2
					y = MARGIN + i * SIDE + SIDE / 2
					original = self.game.start_puzzle[i][j]
					color = "black" if answer == original else "sea green"
					self.canvas.create_text(
						x, y, text=answer, tags="numbers", fill=color
					)

	def __clear_answers(self):
		self.game.start()
		self.canvas.delete("victory")
		self.__draw_puzzle()

	def __cell_clicked(self, event):
		if self.game.game_over:
			return

		x, y = event.x, event.y
		if (MARGIN < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN):
			self.canvas.focus_set()

			row, col = (y - MARGIN) / SIDE, (x - MARGIN) / SIDE

			if (row, col) = (self.row, self.col):
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
		if self.game.gmae_over:
			return
		if self.row >= 0 and self.col >= and event.char in "1234567890":
			self.game.puzzle[self.row][self.col] = int(event.char)
			self.col, self.row = -1, -1
			self.__draw_puzzle()
			self.__draw_cursor()
			"""
			This is where VICTORY would go.  Maybe include a message
			saying that this problem is solvable (or not)?
			"""







class Sudoku_solver(object):
	"""docstring for Sudoku_solver"""
	def __init__(self, arg):
		super(Sudoku_solver, self).__init__()
		#self.S = arg
		self.size = 9

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
		for i in range(0, self.size):
			for j in range(0, self.size):
				if arr[i][j] == 0:
					return False
				if not self.isSafe(arr, arr[i][j], i, j):
					return False
		return True
	
	def isSafe(self, arr, num, i, j):
		# Returns True if a number is safe in spot (no conflict with row, column, or 3x3 square)
		# i, j: Int - these are the Sudoku puzzle (S) indices

		# Check columns
		for j1 in range(0, self.size):
			if j1 != j and arr[i][j1] == num:
				#print("column" + str(num))
				return False

		# Check rows
		for i1 in range(0, self.size):
			if i1 != i and arr[i1][j] == num:
				#print("row" + str(num))
				return False

		# Check 3x3 square
		x1, x2, y1, y2 = self.determineSquare(i, j)


		for i1 in range(y1, y2):
			for j1 in range(x1, x2):
				if j1 != j and i1 != i and arr[i1][j1] == num:
					return False

		return True


	def find_zero(self, arr):
		for i in range(0, self.size):
			for j in range(0, self.size):
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


	def findSolution(self, arr):
		solved, arr = self.solver(arr)
		if solved:
			self.S = arr
			for l in self.S:
				print(l)
			print("SOLVED")
			return self.S
		else:
			print("This cannot be solved")
			return False



class sudoku_matrix_generator(object):
	def generate(self, s):
		s = s.replace(".", "0")
		i = 1
		l = []
		a = []
		for digit in s:
			l.append(int(digit))
			if i >= 9:
				a.append(l)
				l = []
				i = 0
			i += 1
		return a







s = "974236158638091742125487936316754289742908563589362417867125394253649871491073625"
s2= "123456789913456789223456789323456789423456879523456789623456789723456789823456789"
s3 = "3.542.81.4879.15.6.29.5637485.793.416132.8957.74.6528.2413.9.655.867.192.965124.8"
d3 = "365427819487931526129856374852793641613248957974165283241389765538674192796512438"
h1 = "..2.3...8.....8....31.2.....6..5.27..1.....5.2.4.6..31....8.6.5.......13..531.4.."
h2 = "672435198549178362831629547368951274917243856254867931193784625486592713725316489"

invalid = "...........5....9...4....1.2....3.5....7.....438...2......9.....1.4...6.........."
generator = sudoku_matrix_generator()

c = generator.generate(h1)
grid=[[3,0,6,5,0,8,4,0,0], 
		[5,2,0,0,0,0,0,0,0], 
		[0,8,7,0,0,0,0,3,1], 
		[0,0,3,0,1,0,0,8,0], 
		[9,0,0,8,6,3,0,0,5], 
		[0,5,0,0,9,0,6,0,0], 
		[1,3,0,0,0,0,2,5,0], 
		[0,0,0,0,0,0,0,7,4], 
		[0,0,5,2,0,6,3,0,0]]

solver = Sudoku_solver(c)

print(solver.findSolution(c) == generator.generate(h2))





















