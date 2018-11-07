"""
Reverse the bits in a 32 bit number.

Ex: 
Input: 00000000000000000000000000000001
Output: 10000000000000000000000000000000

A: Int
Output: Int
"""


def reverse(self, A):
        B = 0
        for i in range(32):
            B = B << 1
            if A & 1:
                B = B | 1
            A = A >> 1
        return B


        