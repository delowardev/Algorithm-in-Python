def linear_search(needle, haystack):
	for item in enumerate(haystack):
		if(item[1] == needle):
			return item[0]
	return -1