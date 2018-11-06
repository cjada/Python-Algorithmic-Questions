"""
Return all 3 number combinations that sum to 0 in an array.

Ex:
Input = [1, -1, 0, 2, -1, 5]
 
Output = [(-1, 0, 1), (-1, -1, 2)]
"""

def threeSum(self, A):
        """
        A: Int list
        Return: Triplets list
        """
        A.sort()
        triplets = []

        for i in range(0, len(A) - 2):
            l = i + 1
            r = len(A) - 1

            while l < r:
                s = A[i] + A[l] + A[r]

                if s == 0:
                    triplets.append((A[i], A[l], A[r]))
                    l += 1
                    r -= 1

                elif s < 0:
                    l += 1

                else:
                    r -= 1
                    
        return list(set(triplets))