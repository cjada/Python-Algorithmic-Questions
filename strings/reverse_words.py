"""
A simple 1 line function to reverse the order of words in a string, but not the words themselves.

Ex:
Input: "hello world"
Output: "world hello"

Input: String
Output: String
"""

def reverseWords(self, A):
        return " ".join(A.split()[::-1])