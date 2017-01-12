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

		if ptr != None:
			print ptr.data
			while True:
				ptr = ptr.next
				if ptr == self.head:
					break
				print ptr.data


# Code execution starts here
if __name__ == '__main__':
	cll = CircularLinkedList()
	for i in [4, 3 , 2, 1]:
		cll.push(i)
	cll.printList()