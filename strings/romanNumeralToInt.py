"""
Convert a roman numeral to its corresponding integer value.

Ex: IX = 9
XX = 20
XVII = 17

Input: string
Output: Int
"""


def romanToInt(self, A):
        # Conversion dictionary that holds int value and the subtraction numeral 
        rToI = {"I": (1, ""), "V": (5, "I"), "X": (10, "I"), "L": (50, "X"),
        "C": (100, "X"), "D": (500, "C"), "M": (1000, "C")}
        prevR = "-"
        returnInt = 0
        for numeral in A:
            # Unpack the tuple for the current numeral
            value, subtractNumeral = rToI[numeral]
            
            
            # If the previous numeral == the current numeral's subtraction numeral
            # ex: IX (9) or XC (90) or CM (900)
            if prevR == subtractNumeral:
                # need to subtract the previous numeral's value, as it has already been added
                returnInt -= rToI[prevR][0]
                returnInt += value - rToI[prevR][0]
                
            else:
                returnInt += value
                            
            prevR = numeral
            
        return returnInt