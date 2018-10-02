"""
Find the minimum unsorted subarray which, when sorted, causes the whole array to be sorted.

Return the start and end indices of this subarray.  Return [-1] if array is sorted.

Example:
[1, 4, 3, 2, 7, 10]

[4, 3, 2] => [2, 3, 4] => [1, 2, 3, 4, 7, 10]

So, return [1, 3]


"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        B = sorted(A)
        subarray = [-1]
        for i in range(len(A)):
            if A[i] != B[i]:
                if subarray[0] == -1:
                    subarray[0] = i
                    subarray.append(i)
                else:
                    subarray[1] = i
        return subarray