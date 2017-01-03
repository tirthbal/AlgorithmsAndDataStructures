# Node class
class Node:
    # Constructor to initialize the node object
    def __init__(self, data=None):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked list class
class LinkedList:
    # Constructor to initialize the linked list object
    def __init__(self):
        self.head = None

    # Traverse a singly linked list
    def display(self):
        node = self.head
        while node is not None:
            print node.data,
            node = node.next
            if node is not None:
                print '->',
            else:
                print

    # Inserting element in front
    def push(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
        self.display()

    # Inserting element after given node
    def insert_after(self, prev_node, data):
        newnode = Node(data)
        newnode.next = prev_node.next
        prev_node.next = newnode
        self.display()

    # Append node in the end
    def append(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.display()
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = newnode
        self.display()

    # Delete a node given key
    def delete_by_key(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None
        self.display()
        return

    # Delete a node given postion
    def delete_by_position(self, pos):
		if self.head is None:
			print 'No elements to delete. Please add some'
		temp = self.head.next
		count = 1

		if pos == count:
			self.head = self.head.next # First element is always head in the list
			return

		while temp is not None:
			count += 1
			if count == pos:
				break
			prev = temp
			temp = temp.next

		if temp is None:
			print 'No element at this postion'
			return

		prev.next = temp.next
		temp = None

    # Helper to find the length recursively
    def len_help(self, ptr):
    	if not ptr:
    		return 0
    	return 1 + self.len_help(ptr.next)

    # Find length of linked list recursively
    def length_recur(self):
    	return self.len_help(self.head)

    # Find length iteratively
    def length(self):
    	count = 0
    	ptr = self.head
    	while ptr is not None:
    		count += 1
    		ptr = ptr.next
    	return count

    # Swap two nodes
    def swap_nodes(self, x, y):
    	if not self.head:
    		return
    	if x == y:
    		return
    	prevX , curX = None, self.head
    	while curX and curX.data != x:
    		prevX = curX
    		curX = curX.next

    	prevY, curY = None, self.head
    	while curY and curY.data != y:
    		prevY = curY
    		curY = curY.next

    	if not curX or not curY:
    		return

    	if prevX:
    		prevX.next = curY
    	else:
    		self.head = curY

    	if prevY:
    		prevY.next = curX
    	else:
    		self.head = curX

    	temp = curX.next
    	curX.next = curY.next
    	curY.next = temp

    def reverse(self):
    	prev = None
    	cur = self.head
    	while cur is not None:
    		nxt = cur.next
    		cur.next = prev
    		prev = cur
    		cur = nxt
    	self.head = prev

    def reverseRecur(self, ptr):
    	if ptr is None:
    		return
    	first = ptr
    	if first.next is None:
    		return
    	self.reverseRecur(first.next)
    	first.next.next = ptr
    	first.next = None
    	self.head = ptr.next



def merge_sorted_linked_list(list1, list2):
	list3 = LinkedList()
	list3.head = Node()
	cur_ptr = list1.head
	src_ptr = list2.head
	if cur_ptr.data < src_ptr.data:
		list3.head.data = cur_ptr.data
		cur_ptr = cur_ptr.next
	else:
		list3.head.data = src_ptr.data
		src_ptr = src_ptr.next
	while cur_ptr and src_ptr:
		if cur_ptr.data < src_ptr.data:
			list3.append(cur_ptr.data)
			cur_ptr = cur_ptr.next
		else:
			list3.append(src_ptr.data)
			src_ptr = src_ptr.next

	while cur_ptr:
		list3.append(cur_ptr.data)
		cur_ptr = cur_ptr.next

	while src_ptr:
		list3.append(src_ptr.data)
		src_ptr = src_ptr.next

	return list3




# Code execution starts here
if __name__ == '__main__':
    # Start with empty list
    # llist = LinkedList()
    # llist.head = Node(1)
    # second = Node(2)
    # third = Node(3)
    # # Three nodes have been created
    # llist.head.next = second
    # second.next = third
    # # Inseting two nodes in front
    # llist.push(0)
    # llist.push(-1)
    # # Appending new node
    # llist.append(4)
    # llist.append(5)
    # # Delete -1, 3
    # llist.delete_by_key(-1)
    # llist.delete_by_key(3)
    # # Appending new node
    # llist.append(6)
    # llist.append(7)
    # # Deleting element at 3rd postion
    # llist.delete_by_position(1)
    # # Length of linked list (recursively)
    # print llist.length_recur()
    # # Length of linked list iteratively
    # print llist.length()
    # # Swap node with data 2 and node with data 6
    # llist.swap_nodes(1, 7)
    # # Reverse a linked list
    # llist.reverse()
    # # Reverse a linked list recursively
    # llist.reverseRecur(llist.head)
    # llist.display()
    # Merging two linked list
    llist2 = LinkedList()
    llist3 = LinkedList()
    # Appending data in llist2
    llist2.append(5)
    llist2.append(10)
    llist2.append(15)
    # Display 2nd list
    llist2.display()
    # Appending data in llist3
    llist3.head = Node(2)
    llist3.append(3)
    llist3.append(20)
    # Display 3rd list
    llist3.display()
    merged = LinkedList()
    merged = merge_sorted_linked_list(llist2, llist3)
    merged.display()

