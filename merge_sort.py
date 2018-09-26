def merge_sort(arr):

	if len(arr) < 2:
		return arr

	mid = int(len(arr) / 2)
	left = merge_sort(arr[:mid])
	right = merge_sort(arr[mid:])

	result = []
	i = 0
	j = 0

	while i < len(left) and j < len(right):
		if left[i] > right[j]:
			result.append(right[j])
			j += 1
		else:
			result.append(left[i])
			i += 1


	result += left[i:]
	result += right[j:]

	return result




