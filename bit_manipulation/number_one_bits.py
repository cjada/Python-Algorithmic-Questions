"""
Return the number of 1 bits in a number.

Ex:
9 (1001) has 2 one bits.  So return 2.

Input: A = Int
Output: Int
"""

def numSetBits(self, A):
        num_bits = 0
        while A > 0:
            num_bits += A & 1
            A = A >> 1
        
        return num_bits