

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

	def leaders(self):
		# Leaders are those element in array 
		# which are greater than element on the right side
		length = len(self.array)
		cur_max = self.array[-1]
		ans = []
		for i in range(length - 1, -1, -1):
			if self.array[i] > cur_max:
				ans.append(cur_max)
				cur_max = self.array[i]

		return ans

	def sum_pair_x(self, x):
		# Method find the pair with sum equal to x
		hash_map = set()
		for i in self.array:
			if x - i in hash_map:
				return i, x - i
			hash_map.add(i)
		return None, None

	def majority(self):
		hash_map = {}
		for i in self.array:
			if str(i) in hash_map:
				hash_map[str(i)] += 1
				if hash_map[str(i)] >= len(self.array)/2:
					return i
			else:
				hash_map.update({str(i): 1})

		return None





