"""
Return 1 if the input string is a palindrome, else return 0.

Ex:
Input: "race a car"
Output: 0

Input: "AB.cd:cba"
Output: 1

"""


def isPalindrome(self, A):
        A = A.lower().replace(" ", "")
        A = ''.join([x for x in A if x.isalnum()])
        if A == A[::-1]:
            return 1
        return 0