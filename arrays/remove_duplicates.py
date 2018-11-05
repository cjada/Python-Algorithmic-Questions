"""
Remove the duplicates from an input array A, and return the length of A after the duplicates have been removed.

Input: A = Int list
Output: Int
"""

def remove_duplicates(self, A):
        if len(A) == 1:
            return A
        j = 0
        for i in range(0, len(A)-1):
            if A[i] != A[i+1]:
                A[j] = A[i]
                j += 1
        
        A[j] = A[i+1]
        j += 1
        A = A[:j]
        return len(A)