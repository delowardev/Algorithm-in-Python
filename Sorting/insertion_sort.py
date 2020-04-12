def insertion_sort(L):
	n = len(L)
	for n in range(n):
		j = n
		while j > 0 and L[j] < L[j - 1]:
			L[j], L[j - 1] = L[j - 1], L[j]
			j = j - 1

"""
arr = [10, 5, 2, 8, 7]
insertion_sort(arr)
print(arr) # [2, 5, 7, 8, 10]
"""