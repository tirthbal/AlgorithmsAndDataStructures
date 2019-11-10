# In this implementation we need to find the metric that
# which operation on stack will be more frequent push or pop
# so in this implementation we will make less frequent stack operation
# costly

from queue_ll import Queue


class Stack:

	def __init__(self):
		self.q1 = Queue()
		self.q2 = Queue()


	def push(self, data):
		self.q2.enqueue(data)
		while self.q1.get_front():
			self.q2.enqueue(self.q1.dequeue())
		self.q1, self.q2 = self.q2, self.q1
		self.q2 = Queue()

	def pop(self):
		return self.q1.dequeue()

	def get_top(self):
		return self.q1.get_front()


if __name__ == '__main__':
	st = Stack()
	for i in [3, 2, 1, 4]:
		st.push(i)
	while st.get_top():
		print st.pop()