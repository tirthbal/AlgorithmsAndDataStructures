class Node:
	def __init__(self, data=None):
		self.left = None
		self.right = None
		self.data = data


class Tree:

	def __init__(self, data):
		self.root = Node(data)