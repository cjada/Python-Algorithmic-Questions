"""
Give the output for a string printed in ZigZag form, in a single string (with no spaces).

This output string is to be read line by line.

Example:
A = ABCD, B = 2
A...C.
..B..D

output would be: ACBD

Another example:
A = PAYPALISHIRING, B = 3

P.......A........H.......N
..A..P....L....S....I...I....G
....Y.........I........R

output: PAHNAPLSIIGYIR


Solution is O(n) complexity.
"""


def convert(self, A, B):
        temp = ["" for x in range(B)]
        i = 0
        increase = True
        for char in A:
            temp[i] += char
            if i == 0:
                increase = True
            elif i == B-1:
                increase = False
            
            i = i + 1 if increase else i - 1
        
        return "".join(temp)



