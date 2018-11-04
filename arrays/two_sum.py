"""
Finds if 2 numbers in an array sum to the target.

Input: 
l = list
target = Int

Output: 
Bool
"""

def two_sum(l, target):
	l.sort()

	left = 0
	right = len(l) - 1

	while left < right:
		s = l[left] + l[right]
		if s == target:
			return True

		elif s < target:
			left += 1

		else:
			right -= 1

	return False


