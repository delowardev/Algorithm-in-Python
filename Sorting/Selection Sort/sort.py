

def selection_sort(L):
	n = len(L)
	for i in range(0, n - 1):
		index_min = i
		for j in range(i+1, n):
			if L[j] < L[index_min]:
				index_min = j
		if index_min != i:
			L[i], L[index_min] = L[index_min], L[i]
			 

"""
arr = [2, 1, 3]
selection_sort(arr)
print(arr) #[1, 2, 3]
"""
