from linked_list import Node


class Queue:

	def __init__(self):
		self.front = Node()
		self.rear = self.front

	def enqueue(self, data):
		if not self.front.data:
			self.front.data = data
			self.rear = self.front
			return
		newNode = Node()
		newNode.data = data
		self.rear.next = newNode
		self.rear = self.rear.next

	def dequeue(self):
		if not self.front:
			print 'Queue is empty.'
			return
		ele = self.front.data
		self.front = self.front.next
		return ele

	def get_front(self):
		if not self.front:
			return None
		return self.front.data


if __name__ == '__main__':
	qu = Queue()
	for i in [10, 20, 30, 40, 50]:
		qu.enqueue(i)

	while qu.get_front():
		print qu.dequeue()