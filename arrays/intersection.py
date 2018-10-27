"""
Find the intersection of 2 arrays.

Ex:
A = [1, 2, 3, 4, 5]
B = [2, 4. 8]

Output:
[2, 4]

"""


def intersect(self, A, B):
        i = 0
        j = 0
        intersection = []
        
        while i < len(A) and j < len(B):
            if A[i] == B[j]:
                intersection.append(A[i])
                i += 1
                j += 1
            
            elif A[i] > B[j]:
                j += 1
            
            else:
                i += 1
        
        return intersection