"""
Given a sequence 1, 11, 21, 1211...

1 = "One One" = 11
11 = "Two Ones" = 21
21 = "One Two, One One" = 1211
1211 = "One One, One Two, Two Ones" = 111221

Following this pattern, this function returns the nth sequence (n = 1: 1, n = 2: 11...) as a string.

Input: A = int
Output: String
"""


def countAndSay(self, A):
        seq = "1"
        for n in range(A-1):
            newSeq = ""
            prevChar = seq[0]
            count = 0
            for char in seq:
                if char == prevChar:
                    count += 1
                else:
                    newSeq += str(count) + str(prevChar)
                    prevChar = char
                    count = 1
            
            newSeq += str(count) + str(prevChar)
            seq = newSeq
            
        return seq