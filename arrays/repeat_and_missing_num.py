class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        d = {}
        A_B = []
        for num in A:
            if num in d:
                A_B.append(num)
                break
            d[num] = num
        
        s1 = sum(A) - A_B[0]
        s2 = sum(x for x in range(1, len(A)+1))
        A_B.append(s2-s1)
        return A_B