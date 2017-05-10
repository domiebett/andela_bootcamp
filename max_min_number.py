def find_max_min(numbers):
	max = numbers[0]
	min = numbers[0]

	for i in range (1, len(numbers)):
		if numbers[i] > max:
			max = numbers[i]
		elif numbers[i] < min:
			min = numbers[i]

	if min == max:
		return [max]
	return [min, max]