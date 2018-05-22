class BinarySearch(list):

	#init method with a as the length of list and b as the
	#step of elements in the array

	def __init__(self, a, b):
		
		#initialises the Binary Search class as list

		super(BinarySearch, self).__init__()

		#creates a list of a length with b spacing between
		#the elements

		for i in range(1, a+1):
			self.append(i * b)

		self.length = len(self)

	#search method implementing binary search algorithm
	#with the parameter value as the element to be searched for.

	def search(self, value):
		first = 0
		last = len(self) -1
		count = 0
		found = False
		index = 0

		#finds out if value is the first or last element in the 
		#list

		if value == self[first]:
			index = first
			found = True
		elif value == self[last]:
			index = last
			found = True

		#determines if value is not in the list

		if value not in self:
			return {"count": count, "index": -1}

		#The binary search algorithm. Finds the middle number in list
		#and determines if it is equal to the value being searched for.

		while first<=last and not found:
			midpoint = (first + last) // 2

			if self[midpoint] == value:
				found = True
				index = midpoint
			else:
				count+=1
				if value < self[midpoint]:
					last = midpoint -1
				else: 
					first = midpoint + 1

		#creates a dictionary object containing appropriate info on
		#number of times the code ran (count) and the index of the 
		#value in the list. If not found, returns index as "-1"

		if found:
			dictionary = {"count": count, "index": index}
		else:
			dictionary = {"count": count, "index": -1}

		return dictionary
