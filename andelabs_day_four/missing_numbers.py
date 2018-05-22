def find_missing(list1, list2):

	#returns all elements in list 1 that are not in list2 if
	#list1 is greater than list2

	if len(list1) > len(list2):
		list3 = [x for x in list1 if x not in list2]
		return list3[0]

	#returns all elements in list 2 that are not in list1 if
	#list2 is greater than list1

	elif len(list2) > len(list1):
		list3 = [x for x in list2 if x not in list1]
		return list3[0]

	#returns 0 if list1 and list2 have the same elements
	else:
		return 0