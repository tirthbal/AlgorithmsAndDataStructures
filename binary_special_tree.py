from queue_ll import Queue
from stack_ll import Stack

class Node:
	def __init__(self, data=None):
		self.left = None
		self.right = None
		self.next_right = None
		self.data = data


class BinarySpecialTree:

	def __init__(self):
		self.root = Node()