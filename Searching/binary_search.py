def binary_search(needle, haystack):
	low, high = 0, len(haystack)
	found = False
	while low <= high and not found:
		middle = (low + high) // 2
		middle_item = haystack[middle]
		if middle_item == needle:
			found = True
		else:
			if needle < middle_item:
				high = middle - 1
			else: 
				low = middle + 1

	
	return found

"""
print(binary_search(1, [1,2,3,4,5,6])) 
"""