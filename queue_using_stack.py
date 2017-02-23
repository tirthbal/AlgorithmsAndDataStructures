from stack_ll import Stack_ll


class Queue:

	def __init__(self):
		self.st1 = Stack_ll()
		self.st2 = Stack_ll()


	def enqueue(self, data):
		while self.st1.get_top():
			self.st2.push(self.st1.pop())
		self.st1.push(data)
		while self.st2.get_top():
			self.st1.push(self.st2.pop())


	def dequeue(self):
		return self.st1.pop()

	def get_front(self):
		return self.st1.get_top()



if __name__ == '__main__':
	qu = Queue()
	for i in [1,3,2,4]:
		qu.enqueue(i)

	while qu.get_front():
		print qu.dequeue()