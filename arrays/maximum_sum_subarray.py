def maxSubArray(self, A):
        """
        A: int list
        Return: int
        
        This function returns the maximum sum from any of the contiguous subarrays, assuming there is always at 
        least one integer in the list.
        """

        maximumNums = [A[0]]
        i = 1

        while i < len(A):
            c = maximumNums[i-1] + A[i]
            if A[i] > c:
                maximumNums.append(A[i])
            else:
                maximumNums.append(c)
            i += 1
            
        return max(maximumNums)