def intToRoman(self, A):
        # Conversion list, contains each int value with corresponding roman numeral
        i_to_r = [(1, "I"), (4, "IV"), (5, "V"), (9, "IX"), (10, "X"),
            (40, "XL"), (50, "L"), (90, "XC"), (100, "C"), (400, "CD"),
            (500, "D"), (900, "CM"), (1000, "M")
            ]
        roman_numeral = ""
        i = len(i_to_r) - 1
        while A > 0:
            value, numeral = i_to_r[i]
            if value <= A:
                roman_numeral += numeral
                A -= value
            else:
                i -= 1
        
        return roman_numeral