
class Two_Stacks:

	# constructor for the this class
	def __init__(self):
		self.container = [0 for i in range(0, 30)]
		self.capacity_first = len(self.container)/2
		self.capacity_second = len(self.container)
		self.top_first = -1
		self.top_second = self.capacity_first - 1

	# push in first stack
	def push_first(self, data):
		if self.top_first + 1 >= self.capacity_first:
			print 'First stack overflow'
			return
		self.top_first = self.top_first + 1
		self.container[self.top_first] = data

	# push in second stack
	def push_second(self, data):
		if self.top_second + 1 >= self.capacity_second:
			print 'Second stack overflow'
			return
		self.top_second = self.top_second +  1
		self.container[self.top_second] = data

	# pop from first stack
	def pop_first(self):
		if self.top_first == -1:
			print 'First stack underflow'
			return
		ele = self.container[self.top_first]
		self.top_first = self.top_second - 1
		return ele

	# pop from second stack
	def pop_second(self):
		if self.top_second == self.capacity_first:
			print 'Second stack underflow'
			return
		ele = self.container[self.top_second]
		self.top_second = self.top_second - 1
		return ele

	# get top from first stack
	def get_top_first(self):
		return self.container[self.top_first]

	# get top from second stack
	def get_top_second(self):
		return self.container[self.top_second]


if __name__ == '__main__':
	ts = Two_Stacks()
	ts.push_first(1)
	ts.push_second(5)
	ts.push_first(3)
	ts.push_second(7)
	print ts.pop_first()
	print ts.pop_second()