from queue_ll import Queue
from stack_ll import Stack

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

	def inorder_without_recursion(self):
		if not self.root:
			return
		st = Stack_ll()
		st.push(self.root)
		curnode = self.root
		while st.get_top():
			curnode = st.get_top()
			while curnode.left:
				st.push(curnode.left)
				curnode = curnode.left

			print curnode.data
			curnode = st.get_top()
			st.pop()
			print curnode.data
			if curnode.right:
				st.push(curnode.right)

	def morris_traversal(self):
		current = self.root
		if not current:
			return 

		while current is not None:

			if current.left is None:
				print current.data
				current = current.right
			else:
				pre = current.left
				while pre.right is not None and pre.right != current :
					pre = pre.right
				if pre.right is None:
					pre.right = current
					current = current.left
				else:
					pre.right = None
					print current.data
					current = current.right


# Creating binary tree from the inorder and preorder traversal
def buid_tree(in_order, in_start, in_end, pre_order, pre_ind):

	if in_start > in_end:
		return None
	new_Tree = Node()
	root_data = pre_order[pre_ind]
	try:
		root_index = in_order.index(root_data)
	except ValueError:
		root_index = None
		return None
	new_Tree.data = root_data
	new_Tree.left = build_tree(in_order, in_start, root_index - 1, pre_order, pre_ind + 1)
	new_Tree.right = build_tree(in_order, root_index + 1, in_end, pre_order, pre_ind + 1)
	return new_Tree





		
