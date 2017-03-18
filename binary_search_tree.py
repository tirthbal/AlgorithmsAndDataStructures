
class Node:
	def __init__(self):
		self.left = self.right = None
		self.data = None


class BinarySearchTree:

	def __init__(self):
		self.root = Node()

	def __search_helper(self, curnode, target):
		if not curnode:
			return None
		if curnode.data == target:
			return curnode
		if curnode.data < target:
			return self.__search_helper(curnode.right, target)
		else:
			return self.__search_helper(curnode.left, target)

	def search(self, target):
		return self.__search_helper(self.root, target)
	