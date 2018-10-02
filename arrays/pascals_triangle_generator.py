import math

class pascal_triangle:
	def pacscal_generator(self, n, k):
		"""
		Computes the digit at the nth row, kth column.  0 based indexing.
		n: int
		k: int
		Return: int
		"""
		return int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))
		
	def create(self, A):
		"""
		Creates Pascal's triangle up to A rows
		A: int
		Return: 2D list
		"""

		output = []
		for i in range(0, A):
			level = []
			for j in range(0, i+1):
				level.append(self.pacscal_generator(i, j))
			output.append(level)
		return output




