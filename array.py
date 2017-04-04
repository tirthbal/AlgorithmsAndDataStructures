

class Array:

	def __init__(self):
		self.array = []


	def linear_search(self, key):

		for i in self.array:
			if i == key:
				print 'Key found'
		print 'Key not found'


	def binary_search(self, key):

		beg,end = 0, len(self.array)

		while beg <= end:
			mid = (beg + end)/2
			if self.array[mid] == key:
				print 'Key found'
				break
			elif self.array[mid] < key:
				beg = mid + 1
			else:
				end = mid - 1

		print 'Key not found' 
