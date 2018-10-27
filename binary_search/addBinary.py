"""
Add two binary strings together, and return their sum (also a binary string).

Ex: 
Input: 110
       101

Return: 1011

Inputs: A = String
        B = String

Output: String
"""

def addBinary(self, A, B):
        # Equalize the strings by inserting 0's to the front of whatever binary string is shorter
        if len(A) < len(B):
            A = "0" * (len(B) - len(A)) + A

        elif len(B) < len(A):
            B = "0" * (len(A) - len(B)) + B
        
        i = len(A) - 1
        binStr = ""
        carry = False  # True when there is an overflow (1 + 1)

        while i >= 0:
            if A[i] == "1" and B[i] == "1":
                if carry:
                    binStr = "1" + binStr
                else:
                    binStr = "0" + binStr
                    carry = True
            
            elif A[i] == "0" and B[i] == "0":
                if carry:
                    binStr = "1" + binStr
                else:
                    binStr = "0" + binStr
                carry = False
            
            else:
                binStr = "0" + binStr
                
        
            i -= 1

        if carry:
            binStr = "1" + binStr
            
        return binStr





