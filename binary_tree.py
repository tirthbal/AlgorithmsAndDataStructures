from queue_ll import Queue

class Node:
	def __init__(self, data=None):
		self.left = None
		self.right = None
		self.data = data


class Tree:

	def __init__(self, data):
		self.root = Node(data)

	def inorder(self, curnode):
		if not curnode:
			return
		self.inorder(curnode.left)
		print curnode.data
		self.inorder(curnode.right)

	def preorder(self, curnode):
		if not curnode:
			return
		print curnode.data
		self.preorder(curnode.left)
		self.preorder(curnode.right)

	def postorder(self, curnode):
		if not curnode:
			return
		self.postorder(curnode.left)
		self.postorder(curnode.right)
		print curnode.data

	def bfs(self):
		if not self.root:
			return 
		qu = Queue()
		qu.enqueue(self.root)
		while qu.get_front():
			curnode = qu.dequeue()
			print curnode.data
			qu.enqueue(curnode.left)
			qu.enqueue(curnode.right)
	
	def height(self, curnode):
		if not curnode:
			return 0
		
		lheight = height(curnode.left) + 1
		rheight = height(curnode.right) + 1

		if lheight < rheight:
			return rheight
		else:
			return lheight

	def __level_order_helper(self, curnode, level):
		if not curnode:
			return
		if level == 1:
			print curnode.data
		else:
			self.__level_order_helper(curnode.left, level - 1)
			self.__level_order_helper(curnode.right, level - 1)

	def level_order(self):
		height_of_tree = self.height(self.root)
		for i in range(1, height_of_tree + 1):
			self.__level_order_helper(self.root, i)

	def diameter(self, curnode):
		if not curnode:
			return 0
		lheight = self.height(curnode.left)
		rheight = self.height(curnode.right)
		ldiameter = self.diameter(curnode.left)
		rdiameter = self.diameter(curnode.right)
		max_diameter = max(ldiameter, rdiameter)
		max_diameter = max(max_diameter, lheight + rheight + 1)
		return max_diameter




		
