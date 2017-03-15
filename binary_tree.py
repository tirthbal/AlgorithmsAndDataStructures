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


	def width(self):
		# Width of tree is defined as the maximum number of node at
		# any level of the tree
		q = []
		q.insert(0, self.root)
		max_width = 0
		while q != []:
			count = len(q)
			max_width = max(count, max_width)
			while count != 0 :
				count  = count - 1
				tmp = q[0]
				q.pop()
				if tmp.left is not None:
					q.insert(0, tmp.left)
				if tmp.right is not None:
					q.insert(0, tmp.right)
		return max_width

	def get_width_of_current_level(self, node, level):
		if node is None:
			return 0
		if level == 1:
			return 1
		ans  = self.get_width_of_current_level(node.left, level - 1)
		ans += self.get_width_of_current_level(node.right, level - 1)
		return ans

	def width_recur(self):
		max_width = 0
		height = self.height()
		for i in range(1, height + 1):
			cur_width = self.get_width_of_current_level(root, i)
			max_width = max(max_width, cur_width)
		return max_width

	def k_dis_helper(self, curnode, k):
		if not curnode:
			return
		if k == 0:
			print curnode.data
			return
		self.k_dis_helper(curnode.left, k - 1)
		self.k_dis_helper(curnode.right, k - 1)

	def print_node_at_k_dis(self, k):
		self.k_dis_helper(self.root, k)

	def print_ancestors_of_a_node(self, node_value):
		if not self.root:
			return
		node_qu = Queue()
		ancestor_list_qu = Queue()
		node_qu.enqueue(self.root)
		ancestor_list_qu.enqueue([])
		while node_qu.get_front():
			curnode = node_qu.get_front()
			if curnode.data == node_value:
				print ancestor_list_qu.get_front()
				break
			if curnode.left:
				node_qu.enqueue(curnode.left)
				tmp = ancestor_list_qu.get_front()
				tmp += [curnode.data]
				ancestor_list_qu.enqueue(tmp)
			if curnode.right:
				node_qu.enqueue(curnode.right)
				tmp = ancestor_list_qu.get_front()
				tmp += [curnode.data]
				ancestor_list_qu.enqueue(tmp)
			node_qu.dequeue()
			ancestor_list_qu.dequeue()

	def print_ancestors_helper(self, curnode, target):
		if not curnode:
			return false
		if curnode.data == target:
			return true
		if (self.print_ancestors_helper(curnode.left, target) or
			self.print_ancestors_helper(curnode.right, target)):
			print curnode.data
			return true

	def print_ancestors_of_node_recur(self, node_value):
		self.print_ancestors_helper(self.root, node_value)










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





		
