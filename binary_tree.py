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
	
		
