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
			return

		# Traversing till last node
		ptr = self.head
		while ptr.next:
			ptr = ptr.next

		# Make last node as prev element of last node
		new_node.prev = ptr

		# Make new node as last node
		ptr.next = new_node


	def insert_after(self, prev_node, data):

		# Initializing a new node
		new_node = Node(data)

		# Saving the cur next node of prev node
		next_node = prev_node.next

		# Make new node as new next node of prev node
		prev_node.next = new_node

		# Make prev next node as next node of new node
		new_node.next = next_node

		# Make new node as prev for prev_node next node
		if next_node:
			next_node.prev = new_node

		# Make prev node as prev node of new node
		new_node.prev = prev_node


	# Print dll from Left to Right
	def print_forward(self):

		# Starting traversal from the begining
		cur_ptr = self.head

		op = ''
		while cur_ptr != None:
			op += ' -><- ' if op else ''
			op += str(cur_ptr.data)
			cur_ptr = cur_ptr.next

		print op


	# Print dll from right to left
	def print_backward(self):

		# To do so we need to first traverse upto 
		# last node
		cur_ptr = self.head

		while cur_ptr.next != None:
			cur_ptr = cur_ptr.next

		# Traversing backward using prev ptr of node
		op = ''
		while cur_ptr != None:
			op += ' -><- ' if op else ''
			op += str(cur_ptr.data)
			cur_ptr = cur_ptr.prev

		print op


	# Delete from begining of DLL
	def delete_head(self):

		# Save the cur head node data
		ptr = self.head.data

		# Make 2nd node as new head node
		next_node = self.head.next
		next_node.prev = None
		self.head = next_node

		return ptr


	# Delete last node
	def delete_last(self):

		# traverse till last node 
		cur_ptr = self.head

		while cur_ptr.next != None :
			cur_ptr = cur_ptr.next

		# save data of last node
		tmp = cur_ptr.data

		cur_ptr.prev.next = None

		cur_ptr.prev = None
		
		return tmp


	# Delete a given node
	def delete_given_node(self, ptr):

		# make the next of previous node equals to next of 
		# the node to be deleted
		ptr.prev.next = ptr.next

		ptr.next.prev = ptr.prev

		return ptr.data



	# Reverse Dll
	def reverse(self):

		tmp = None
		cur_ptr = ptr = self.head

		# swap the next and prev of every node
		while cur_ptr != None:
			tmp = cur_ptr.prev
			cur_ptr.prev = cur_ptr.next
			cur_ptr.next = tmp
			cur_ptr = cur_ptr.prev

		if tmp:
			self.head = tmp.prev

	def partition(self, start, end):
		pivot = start
		beg = start.next
		cur_p = start.next
		prev_p = cur_p
		if not cur_p:
			return prev_p
		while end.next != beg:
			if beg.data < pivot.data:
				cur_p.data, beg.data = beg.data, cur_p.data
				prev_p = cur_p
				cur_p = cur_p.next
			beg = beg.next
		if start.data > prev_p.data:
			start.data, prev_p.data = prev_p.data, start.data
		return prev_p

	def _quick_sort(self, start, end):
		if start is None or end is None:
			return
		if start == end or end.next == start:
			return
		p = self.partition(start, end)
		self._quick_sort(start, p.prev)
		self._quick_sort(p.next, end)

	# Quick sort in dll
	def quick_sort(self):
		ptr = self.head
		while ptr.next != None:
			ptr = ptr.next
		self._quick_sort(self.head, ptr)


# Code execution starts here
if __name__ == '__main__':
	dll = DoubleLinkedList()
	# for i in [5, 4, 3, 2, 1]:
	# 	dll.insert_at_beg(i)

	# dll.print_forward()
	# dll.print_backward()

	# for i in [6, 7, 8, 9, 10]:
	# 	print i
	# 	dll.insert_at_end(i)

	# dll.print_forward()
	# # print dll.delete_head()
	# # print dll.delete_last()
	# dll.print_forward()

	# # dll.reverse()
	# dll.print_forward()
	# 4, 6, 5, 2, 10, 8, 1, 7, 3, 9
	for i in [4, 6, 5, 2, 10, 8, 1, 7, 3, 9]:
		dll.insert_at_end(i)
	dll.quick_sort()
	dll.print_forward()
	dll2 = DoubleLinkedList()
	for i in [4, 5, 6, 7, 1, 2, 3]:
		dll2.insert_at_end(i)
	dll2.quick_sort()
	dll2.print_forward()

	dll3 = DoubleLinkedList()
	for i in [1, 2, 3, 4, 5, 6, 7, 8]:
		dll3.insert_at_end(i)
	dll3.quick_sort()
	dll3.print_forward()



