# Node class
class Node:
    # Constructor to initialize the node object
    def __init__(self, data=None):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null

# Circular Linked List
class CircularLinkedList:

	# Constructor for circular linked list
	def __init__(self):
		self.head = None

	# Insert node in the begining of circular linked list
	def push(self, data):
		ptr = Node(data)
		temp = self.head

		ptr.next = self.head

		if self.head is not None:
			while (temp.next != self.head):
				temp = temp.next
			temp.next = ptr
		else:
			ptr.next = ptr

		self.head = ptr

	# Traversal in the circular linked list
	def printList(self):
		ptr = self.head
		op = ''
		if ptr != None:
			op += str(ptr.data)
			while True:
				ptr = ptr.next
				if ptr == self.head:
					break
				op += ' -> ' + str(ptr.data)
		print op

	def split_cll_in_two(self, head1, head2):
		slwptr = self.head
		fastptr = self.head

		if not self.head:
			return

		# If htere are odd nodes in the circular list then
        # fast_ptr->next becomes head and for even nodes
        # fast_ptr->next->next becomes head
		while (fastptr.next != self.head and fastptr.next.next != self.head):
			fastptr = fastptr.next.next
			slwptr = slwptr.next

		# If there are even nodes
		if fastptr.next.next == self.head:
			fastptr = fastptr.next

		# Set the head of first halve
		head1.head = self.head

		# Set the head of second halve
		if self.head.next != self.head:
			head2.head = slwptr.next

		# Make the second half circular
		fastptr.next = slwptr.next

		# Make the first halve circular
		slwptr.next = self.head

	def insert_in_sorted(self, data):
		if not self.head:
			self.push(data)
			return
		if self.head.data > data:
			self.push(data)
			return
		new_node = Node(data)

		cur_node = self.head
		while cur_node.next != self.head and cur_node.next.data < new_node.data:
			cur_node = cur_node.next

		new_node.next = cur_node.next
		cur_node.next = new_node



# Code execution starts here
if __name__ == '__main__':
	cll = CircularLinkedList()
	for i in [5, 4, 3 , 2, 1]:
		cll.push(i)
	cll.printList()
	head1 = CircularLinkedList()
	head2 = CircularLinkedList()
	cll.split_cll_in_two(head1, head2)
	head1.printList()
	head2.printList()
	new_cll = CircularLinkedList()
	for i in [3, 5, 4, 1, 2]:
		new_cll.insert_in_sorted(i)
	new_cll.printList()
