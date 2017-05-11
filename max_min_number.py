def find_max_min(numbers):

	#initial values for maximum and minimum numbers initialised to
	#first item in a list.

	max = numbers[0]
	min = numbers[0]

	#loops through the list and sets any number larger than the current
	#value set as max to max less than the current min to min.

	for i in range (1, len(numbers)):
		if numbers[i] > max:
			max = numbers[i]
		elif numbers[i] < min:
			min = numbers[i]

	#if code completes while all numbers are the same, them list is of
	#similar numbers. If not, return a list with max and min.

	if min == max:
		return [max]
	return [min, max]
