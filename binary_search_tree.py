
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



	