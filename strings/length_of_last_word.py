"""
Returns the length of the last word in a string.

Ex:
Input: "hello world"
Output: 5

Input: string
Output: Int
"""

def lengthOfLastWord(self, A):
        wordList = A.split()
        if wordList:
            return len(wordList[-1])
        return 0