"""
Return True if n is a power of 2.  Return False otherwise.
"""

def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        """
		The bitwise operation below works because a power of 2 will only have 1 "on" bit.
        """
        return (n & (n - 1)) == 0


        