from double_linked_list import Node

class Dequeue:

	def __init__(self):
		self.front = self.rear = Node()

	def insert_front(self, data):
		newNode = Node(data)
		if not self.front or not self.front.data:
			self.front = newNode
			self.rear = self.front
			return
		newNode.next = self.front
		self.front.prev = newNode
		self.front = newNode

	def insert_end(self, data):
		newNode = Node(data)
		if not self.rear or not self.rear.data:
			self.rear = newNode
			self.front = self.rear
			return
		newNode.prev = self.rear
		self.rear.next = newNode
		self.rear = newNode

	def delete_front(self):
		if not self.front:
			print 'Dequeue is empty!!'
			return None
		if self.front.next:
			self.front.next.prev = None
		ele = self.front.data
		self.front = self.front.next
		return ele

	def delete_end(self):
		if not self.rear:
			print 'Dequeue is empty!!'
			return None
		if self.rear.prev:
			self.rear.prev.next = None
		ele = self.rear.data
		self.rear = self.rear.prev
		return ele

	def get_front(self):
		if not self.front:
			return None
		return self.front.data

	def get_end(self):
		if not self.rear:
			return None
		return self.rear.data


if __name__ == '__main__':
	dq = Dequeue()
	for i in [1, 2, 3, 4, 5]:
		dq.insert_front(i)

	while dq.get_end():
		print dq.delete_end()

	for i in [1, 2, 3, 4, 5]:
		dq.insert_end(i)

	while dq.get_front():
		print dq.delete_front()


