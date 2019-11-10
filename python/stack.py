# Implementing stack as an array


class Stack:

	# constructor  of stack
	def __init__(self):
		self.top = 0
		self.buffer = []
		self.max_capacity = 1000


	# Push in the stack
	def push(self, data):
		if self.top > self.max_capacity:
			print 'Stack overflow'
			return
		self.buffer.append(data)
		self.top += 1

	# Pop in the stack
	def pop(self):
		if self.top == 0:
			print "stack underflow"
			return
		ele = self.buffer[self.top - 1]
		self.top -= 1
		self.buffer.pop()
		return ele

	# Access self.top element
	def get_top(self):
		if self.top == 0:
			return None
		return self.buffer[self.top - 1]


if __name__ == '__main__':
	st = Stack()
	for i in [3, 2, 1, 4]:
		st.push(i)
	while True:
		ele = st.pop()
		if not ele:
			break
		print ele