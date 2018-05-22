def words(text):

	#splits text to separate strings and makes them a list.

	split_list = text.split()

	#changes all strings that are digits to integers.

	split_list = [int(x) if x.isdigit() else x for x in split_list]
	word_count = {}

	while True:

		length = len(split_list)

		#sets element to the first item in the split list.

		element = split_list[0]
		
		#sets number which increments each code finds a similar element.

		number = 0

		#if function has completed, returns zero.

		if (length <= 0):
			return word_count

		#if list has only one item, returns the items count as 1

		elif(length == 1):
			number = 1
			word_count[element] = 1
			return word_count

		#takes element and compares it to all items in the list

		for i in range(0, len(split_list)):
			if split_list[i] == element:
				number+=1

		#sets count and element in dictionary item.
		
		word_count[element] = number

		#removes the element that has already been counted and returns split
		#list

		split_list[:] = (value for value in split_list if value !=element)
		number = 0
		element = ""
