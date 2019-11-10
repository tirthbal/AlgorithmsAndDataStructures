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

	def connect_right_node(self):
		if not self.root:
			return

		qu = Queue()
		qu.enqueue({node: self.root, level: 1})
		prev_front = {node: None, level: 0}
		while qu.get_front():
			front = qu.get_front()
			qu.enqueue()
			if front.left:
				qu.enqueue({node: front.left, level: front.level + 1})
			if front.right:
				qu.enqueue({node: front.right, level: front.level + 1})
			if not prev_front.node || prev_front.level != front.level:
				prev_front = front
				continue
			prev_front.node.next_right = front
