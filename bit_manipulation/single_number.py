"""
In a list where every number is repeated twice, find the number that only appears once.

Ex: Input = [1, 2, 2, 3, 3, 1, 4]
Output = 4

A: Int List 
Ouput: Int
"""


def singleNumber(self, A):
        n = 0
        for num in A:
            n = n ^ num
        
        return n