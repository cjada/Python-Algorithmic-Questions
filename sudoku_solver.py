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





















