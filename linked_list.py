# Node class
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
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

    # Inserting element after given node
    def insert_after(self, prev_node, data):
        newnode = Node(data)
        newnode.next = prev_node.next
        prev_node.next = newnode

    # Append node in the end
    def append(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = newnode

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
    	return



# Code execution starts here
if __name__ == '__main__':
    # Start with empty list
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    # Three nodes have been created
    llist.head.next = second
    second.next = third
    # Printing the linked list
    llist.display()
    # Inseting two nodes in front
    llist.push(0)
    llist.push(-1)
    # Printing updated list
    llist.display()
    # Appending new node
    llist.append(4)
    llist.append(5)
    # Printing updated list
    llist.display()
    # Delete -1, 3
    llist.delete_by_key(-1)
    llist.delete_by_key(3)
    # Printing updated list
    llist.display()
    # Appending new node
    llist.append(6)
    llist.append(7)
    # Printing updated list
    llist.display()
    # Deleting element at 3rd postion
    llist.delete_by_position(1)
    # Printing updated list
    llist.display()
