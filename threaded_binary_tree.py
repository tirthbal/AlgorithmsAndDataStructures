class Node:

	def __init__(self):
		self.left = None
		self.right = None
		self.right_thread = false


class ThreadedBinaryTree:

	def __init__(self):
		self.root = Node()


	def left_most(self, curnode):
		if not curnode:
			return None
		current = curnode
		while current.left is not None :
			current = current.left
		return current


	def inorder(self):
		current = self.left_most(self.root)

		while current is not None:

			print current.data

			if (current.right_thread):
				current = current.right
			else:
				current = self.left_most(current.right)
