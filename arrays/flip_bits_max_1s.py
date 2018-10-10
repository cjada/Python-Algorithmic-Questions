"""

Flip all bits between two indices L and R, such that 1 <= L <= R <= N (length of the string), so that the 
string with the maximum number of 1s is returned.

"""

class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        if not A:
            return []
        
        temp = [-1 if A[0] == "0" else 1]
        
        # Find the subarray sum with the least value, giving 0's a weight of -1
        for i in range(1, len(A)):
            val = -1 if A[i] == "0" else 1
            if val + temp[i-1] < val:
                temp.append(val + temp[i-1])
            else:
                temp.append(val)
        
        # If the minimum is 1, then return [], as no improvements can be made
        minimum = min(temp)
        if minimum == 1:
            return []
            
        # Find the index of the earliest minimum value in the array
        index = temp.index(minimum)
        
        # Create the output array, with index + 1 (signifying right most index)
        L_R = [0, index + 1]
        
        # Backtrack through the array to find the indices of the minimum subarray
        while index >= 0 and temp[index] <= 0:
            index -= 1
            
        # Add 2, instead of one, due to extra decrement from while loop
        L_R[0] = index + 2
        
        return L_R
        