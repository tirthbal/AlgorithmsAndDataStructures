

class Queue:

	def __init__(self):
		self.capacity = 100
		self.container = [0 for i in range(0, 100)]
		self.front = 0
		self.rear = 0 


	def enqueue(self, data):
		if self.rear == 0:
			self.container[self.rear] = data
			self.rear += 1
			return
		if self.front == self.rear and self.front != 0 :
			print 'Queue Overflow'
			return
		self.container[self.rear] = data
		self.rear = (self.rear + 1) % self.capacity

	def dequeue(self):
		if self.front == self.rear:
			print 'Queue underflow!!'
			return None
		ele = self.container[self.front]
		self.container[self.front] = 0
		self.front += 1
		return ele

	def get_front(self):
		if self.rear == 0:
			print 'Stack is empty'
			return None
		if self.rear == self.front:
			return None
		return self.container[self.front]


if __name__ == '__main__':
	qu = Queue()
	for i in [1,3,2,4]:
		qu.enqueue(i)

	while qu.get_front():
		print qu.dequeue()
