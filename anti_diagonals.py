"""
Find and return the anti diagonals of a NxN matrix.

The anti diagonals are defined as follows:

1 2 3
4 5 6 
7 8 9

Anti Diagonals: [[1], [2, 4], [3, 5, 7], [6, 8], [9]]

Returns a 2D list
"""

class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def findDiag(self, A, i, j):
        # A: Matrix
        # i, j: Int (matrix indices)
        # Return: list
        diag = []
        while j >= 0 and i < len(A):
            diag.append(A[i][j])
            i += 1
            j -= 1
        return diag
    
    def diagonal(self, A):
        diagonals = []
        for j in range(0, len(A)):
            diagonals.append(self.findDiag(A, 0, j))
        for i in range(1, len(A)):
            diagonals.append(self.findDiag(A, i, len(A) - 1))
        
        return diagonals