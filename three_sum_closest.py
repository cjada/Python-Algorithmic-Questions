"""
Return the closest 3 integer sum (in A) to the input target B.

Ex:
A = [1, 2, 3, -3, 0]
B = -2
Output: -1 (-3 + 2 + 0)
"""


def threeSumClosest(self, A, B):
        """
        A: Int list
        B: Int
        Return: Int
        """

        if len(A) < 3:
            return -1
            
        closest_sum = A[0] + A[1] + A[2]
        A.sort()

        for i in range(0, len(A) - 2):
            l = i + 1
            r = len(A) - 1

            while l < r:
                three_sum = A[i] + A[l] + A[r]
                if three_sum == B:
                    return three_sum
                
                if abs(three_sum - B) < abs(closest_sum - B):
                    closest_sum = three_sum
                
                if three_sum < B:
                    l += 1
                
                else:
                    r -= 1
        
        return closest_sum