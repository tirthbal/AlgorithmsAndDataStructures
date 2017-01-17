# Node class
class Node:
    def __init__(self, data=None):
	    self.data = data  # Assign data
	    self.next = None  # Initialize next as null
	    self.prev = None  # Initialize prev as null


class DoubleLinkedList:

	# Construnctor for double linked list
	def __init__(self):
		self.head = None


	# Insert a node in begining of double ll
	def insert_at_beg(self, data):
		
		# Intializing a new node
		new_node = Node(data)

		# Check for dll is empty
		if not self.head:
			self.head = new_node
			return
		
		# Make cur head , next element for new node
		new_node.next = self.head
		
		# Make new node as prev element for cur head
		self.head.prev = new_node
		
		# Make new node as new head
		self.head = new_node


	# Insert a node in the end of double ll
	def insert_at_end(self, data):
		
		# Initializing a new node
		new_node = Node(data)

		# Check for dll is empty
		if not self.head:
			self.head = new_node

		# Traversing till last node
		ptr = self.head
		while ptr.next != None:
			ptr = ptr.next

		# Make last node as prev element of last node
		new_node.prev = ptr

		# Make new node as last node
		ptr.next = new_node


	# Print dll from Left to Right
	def print_forward(self):

		# Starting traversal from the begining
		cur_ptr = self.head

		while cur_ptr != None:
			print cur_ptr.data ,
			cur_ptr = cur_ptr.next


	# Print dll from right to left
	def print_backward(self):

		# To do so we need to first traverse upto 
		# last node
		cur_ptr = self.head

		while cur_ptr.next != None:
			cur_ptr = cur_ptr.next

		# Traversing backward using prev ptr of node
		while cur_ptr != None:
			print cur_ptr.data ,
			cur_ptr = cur_ptr.prev


# Code execution starts here
if __name__ == '__main__':
	dll = DoubleLinkedList()
	for i in [5, 4, 3, 2, 1]:
		dll.insert_at_beg(i)

	dll.print_forward()
	dll.print_backward()

	for i in [6, 7, 8, 9, 10]:
		dll.insert_at_end(i)

	dll.print_forward()


