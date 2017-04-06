

class Array:

	def __init__(self):
		self.array = []


	def linear_search(self, key):

		for i in self.array:
			if i == key:
				print 'Key found'
		print 'Key not found'


	def binary_search(self, key):

		# To use binary search array must be sorted

		beg,end = 0, len(self.array)

		while beg <= end:
			mid = (beg + end)/2
			if self.array[mid] == key:
				print 'Key found'
				return mid
				break
			elif self.array[mid] < key:
				beg = mid + 1
			else:
				end = mid - 1

		print 'Key not found'
		return beg

	def insert_in_sorted(self, key):

		# find the upper bound of the key
		pos = self.binary_search(key)

		# Store the data after pos to end in
		# a temporary buffer
		tmp = []
		for i range(pos, len(self.array)):
			tmp.append(self.array[i])

		# Store the data from start to pos - 1 in the new array
		new_array = self.array[:pos]
		new_array.append(key)
		new_array += tmp
		del tmp
		self.array = new_array

	def delete_in_sorted(self, key):

		# find the pos of the key
		pos = self.binary_search(key)

		self.array = self.array[:pos] + self.array[pos + 1: ]
		


