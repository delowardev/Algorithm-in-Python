def bubble_sort(L):
	n = len(L)
	for i in range(0, n - 1):
		for j in range(0, n - i - 1):
			if L[j] > L[j + 1]:
				L[j], L[j + 1] = L[j + 1], L[j]


"""
arr = [10, 5, 2, 8, 7]
bubble_sort(arr)
print(arr) # [2, 5, 7, 8, 10]
"""