
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




	