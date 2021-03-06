
class Node:
	def __init__(self):
		self.left = self.right = None
		self.data = None


class BinarySearchTree:

	def __init__(self):
		self.root = Node()
		self.inorder_list = []

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

	def __insert_helper(self, curnode, newnode):
		if curnode is None:
			curnode = newnode
		else:
			if root.val < node.val:
				if root.right is None:
					root.right = newnode
				else:
					__insert_helper(root.right, newnode)
			else:
			if root.left is None:
                root.left = node
            else:
                __insert_helper(root.left, node)

    def insert(self, data):
    	newnode = Node()
    	newnode.data = data
    	self.__insert_helper(self.root, newnode)


    def __inorder_helper(self, curnode):
    	if not curnode:
    		return
    	self.__inorder_helper(curnode.left)
    	print curnode.data
    	self.inorder_list.append(curnode.data)
    	self.__inorder_helper(curnode.right)

    def inorder(self):
    	self.__inorder_helper(self.root)
    	return


    def min_value_node(node):
    	current = node
    	while current.left:
    		curnode = current.left
   
    	return current

    def __delete_helper(self, curnode, key):
    	if curnode is None:
    		return 
    	if key < curnode.data:
    		self.__delete_helper(curnode.left, key)
    	elif key > curnode.data:
    		self.__delete_helper(curnode.right, key)
    	else:
    		if curnode.left is None:
    			tmp = curnode.right
    			curnode = tmp
    			return
    		if curnode.right is None:
    			tmp = curnode.left
    			curnode = tmp
    			return

    		tmp = self.min_value_node(curnode)

    		curnode.data = tmp.data

    		curnode.right = self.__delete_helper(curnode.right, key)

    		return


    def delete(self, key):
    	return self.__delete_helper(self.root, key)


    def __find_pre_suc_helper(self, curnode, key):
    	if curnode is None:
    		return

    	if curnode.data == key:

    		if curnode.left is not None:

    			tmp = curnode.left
    			while tmp.right:
    				tmp = tmp.right
    			find_pre_suc.pre = tmp

    		if curnode.right is not None:

    			tmp = curnode.right
    			while tmp.left is not None:
    				tmp = tmp.left
    			find_pre_suc.suc = tmp
    		return
    	elif curnode.data > key:
    		find_pre_suc.suc = curnode
    		self.__find_pre_suc_helper(curnode.left, key)
    	else:
    		find_pre_suc.pre = curnode
    		self.__find_pre_suc_helper(curnode.right, key)


    def find_pre_suc(self, key):
    	self.__find+find_pre_suc_helper(self.root, key)


    def is_bst_helper(self, node, mini, maxi):
    	if node is None:
    		return True

    	if node.data < mini || node.data > maxi:
    		return False

    	return (self.is_bst_helper(node.left, mini, node.data + 1) or 
    		self.is_bst_helper(node.right, node.data - 1, maxi))
    
    def is_bst(self):
    	INT_MAX = 4294967296
		INT_MIN = -4294967296
		retrun self.is_bst_helper(self.root, INT_MIN, INT_MAX)

	def __lca_helper(self, curnode, node_a, node_b):
		if curnode is None:
			return None

		if curnode.data < node_a.data and curnode.data < node_b.data:
			return self.__lca_helper(curnode.right, node_a, node_b)

		if curnode.data > node_a.data and curnode.data > node_b.data:
			return self.__lca_helper(curnode.left, node_a, node_b)

		return curnode

	def lca(self, node_a, node_b):
		return self.__lca_helper(self.root, node_a, node_b)


	def inorder_suc(self, node):

		if node.right is not None:
			return min_value_node(node.right)

		p = node.parent
		n = node
		while p is not None:
			if n != p.right:
				break
			n = p
			p = p.parent

		return p

	def kth_element(self, k):
		self.inorder(self.root)
		return self.inorder_list[k - 1]


	def correct_bst_helper(self, cur_node, prev_node, first, middle, last):
		if curnode is None:
			return

		self.correct_bst_helper(cur_node.left, prev_node, first, middle, last)

		if prev_node is not None and cur_node.data < prev_node.data:

			if first is None:
				first = prev_node
				middle = cur_node
			else:
				last = cur_node
		
		prev_node = cur_node

		self.correct_bst_helper(cur_node.right, prev_node, first, middle, last)

	def correct_bst(self, first=None, middle=None, last=None):
		self.correct_bst_helper(self.root, None, first, middle, last)

		if first is not None and last is not None:
			first.data, last.data = last.data, first.data

		elif first is not None and middle is not None:
			first.data, middle.data = first.data, middle.data

	def __ceil_helper(self, curnode, key):
		if curnode is None:
			return
		if curnode.data == key:
			return curnode

		if curnode.data < key:
			return self.__ceil_helper(curnode.right, key)
		else:
			return self.__ceil_helper(curnode.left, key)

	def ceil(self, key):
		return self.__ceil_helper(self.root, key)


	def pair_with_sum(self, sum):
		self.inorder()
		cur_list = self.inorder_list

		hash_dict = {str(i): true for i in cur_list}

		for i in cur_list:
			tmp = sum - i
			if str(tmp) in hash_dict:
				return (i, tmp)
		return (None, None)



def merge_bsts(bst1, bst2):
	bst1.inorder()
	bst2.inorder()
	inorder_list1 = bst1.inorder_list
	inorder_list2 = bst2.inorder_list
	
	len1 = len(inorder_list1)
	len2 = len(inorder_list2)

	i, j = 0, 0

	while i < len1 and j < len2:

		if inorder_list1[i] < inorder_list2[j]:
			print inorder_list1[i]
			i = i + 1
		else :
			print inorder_list2[j]
			j = j + 1

	while i < len1:
		print inorder_list1[i]
		i = i + 1

	while j < len2:
		print inorder_list2[j]
		j = j + 1


def find_bino_coeff(n, k):

	ans = 1

	# Since C(n, k) = C(n, n - k)
	k = n - k if k > (n - k) else k

	# Calculate value of [n*(n-1)*---*(n-k+1)] / [k*(k-1)*---*1]
	for i in range(0, k):
		ans *= (n - i)
		ans /= (i + 1)

	return ans




def number_of_possible_bst(n):

	# n: number of nodes in bst
	# b_coeff : binomial coefficient of 2*n and n
	b_coeff = find_bino_coeff(2*n, n)

	# ans: number of possible unique bst
	ans = b_coeff/(n + 1)

	return ans


	