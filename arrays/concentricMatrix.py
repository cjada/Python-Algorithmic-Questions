"""
Prints concentric rectangular pattern in a 2d matrix, given an input integer.

Ex: A = 3
Output:

3 3 3 3 3
3 2 2 2 3
3 2 1 2 3
3 2 2 2 3
3 3 3 3 3

A = 2
Output:

2 2 2
2 1 2
2 2 2


Input: Integer (A >= 1)
Output: 2D matrix
"""


def prettyPrint(self, A):
        mat = [[1]]
        odd = 3
        for i in range(2, A + 1):
            temp = [[i for x in range(odd)] for y in range(odd)]
            x = 1
            
            for row in mat:
                temp[x][1:-1] = row
                x += 1
                
            mat = temp
            odd += 2
            
        return mat