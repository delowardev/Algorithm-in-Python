def linear_search(needle, haystack):
	for item in enumerate(haystack):
		if(item[1] == needle):
			return item[0]
	return -1

linear_search('c', ['a', 'b', 'c', 'd'])
# linear_search('e', ['a', 'b', 'c', 'd']) // return -1