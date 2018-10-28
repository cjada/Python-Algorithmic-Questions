"""
Sort red (0), white (1), and blue (2) so that each are adjacent to one another in O(n) time and O(1) space.

Also known as the Dutch Flag Problem.

Input: A = list of integers (0-2)
Output: Sorted list of integers
"""

def sortColors(self, A):
        low = 0
        mid = 0
        high = len(A) - 1
        
        while mid <= high:
            if A[mid] == 0:
                A[low], A[mid] = A[mid], A[low]
                low += 1
                mid += 1
            
            elif A[mid] == 1:
                mid += 1
            
            else:
                A[mid], A[high] = A[high], A[mid]
                high -= 1
        
        return A

