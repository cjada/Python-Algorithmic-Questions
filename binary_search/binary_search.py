"""
This is just a simple binary search function, for practice purposes.

Input: arr = Int list, x = Int
Output: Int list
"""


def binarySearch(arr, x):
	arr.sort()
	l = 0
	m = len(arr) // 2
	r = len(arr) - 1
	print(m)
	while arr[m] != x:
		if l == m and m == r:
			print(str(x) + " doesn't exist in this list.")
			return -1

		if arr[m] < x:
			r = m
			m = ((r - l) // 2) + l

		else:
			l = m
			m = ((r - l) // 2) + l

	print(str(x) + " was found in this list.")
	return x
"""
print("----------")
binarySearch([1,1,1,1,1,1,1,1], 4)
print("----------")
binarySearch([1,2,3,4,5,6,7], 4)
print("----------")
binarySearch([5,3,2,8,1290,32,1,23,54], 54)
print("----------")
"""
binarySearch([1,2], 1)
print("----------")












