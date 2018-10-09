class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        length = len(A)
        maxGap = 0
        LMin = [0] * length
        RMax = [0] * length
        
        LMin[0] = A[0]
        RMax[length-1] = A[length-1]
        
        for i in range(1, length):
            LMin[i] = min(A[i], LMin[i-1])
        
        for i in range(length - 2, -1, -1):
            RMax[i] = max(A[i], RMax[i+1])
        
        i, j = 0, 0
        while (i < length) and (j < length):
            if LMin[i] <= RMax[j]:
                maxGap = max(maxGap, j - i)
                j += 1
            else:
                i += 1
        
        return maxGap