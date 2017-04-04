

class Array:

	def __init__(self):
		self.array = []


	def linear_search(self, key):

		for i in self.array:
			if i == key:
				print 'Key found'
		print 'Key not found'
		return
