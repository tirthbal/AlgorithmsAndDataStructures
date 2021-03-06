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
            self.display()
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

    def removeLoop(self, slwnode):
        ptr1 = self.head
        while True:
            ptr2 = slwnode
            while ptr2.next != slwnode and ptr2.next != ptr1:
                ptr2 = ptr2.next
            if ptr2.next == ptr1:
                break
            ptr1 = ptr1.next
        ptr2.next = None

    def isLoop(self):
        slwptr = self.head
        fastptr = self.head
        while True:
            slwptr = slwptr.next
            if not slwptr:
                return False
            fastptr = fastptr.next.next
            if not fastptr.next.next:
                return False
            if fastptr == slwptr:
                self.removeLoop(slwptr)
                return True

    def isLoopAndRemove(self):
        slwptr = self.head
        fastptr = self.head.next
        while fastptr and fastptr.next:
            if slwptr == fastptr:
                break
            slwptr = slwptr.next
            fastptr = fastptr.next.next

        if fastptr == slwptr:
            slwptr = self.head
            while slwptr != fastptr.next:
                slwptr = slwptr.next
                fastptr = fastptr.next
            fastptr.next = None
            return True
        return False

    def rotate_by_k_anti_clock(self, k):
        len_ll = self.length()
        k = k % len_ll
        ptr = self.head
        data = []
        for i in range(0, k):
            data.append(ptr.data)
            ptr = ptr.next
        new_node = Node(ptr.data)
        self.head = new_node
        ptr = ptr.next
        while ptr:
            new_node.next = ptr
            new_node = new_node.next
            ptr = ptr.next
        for val in data:
            tmp = Node(val)
            new_node.next = tmp
            new_node = new_node.next

    
    # Delete the last node
    def delete_last(self):
        if not self.head:
            return None
        ptr = self.head
        if not ptr.next:
            data = self.head.data
            self.head = None
            return data
        while ptr.next.next:
            ptr = ptr.next
        data = ptr.next.data
        ptr.next = None
        return data

    # Delete the begining node
    def delete_beg(self):
        if not self.head:
            return None
        data = self.head.data
        self.head = self.head.next
        return data












def reverse_group_of_size_k(ll, k):
    ptr = ll.head
    new_list = LinkedList()
    while True:
        cnt = 1
        st = []
        while cnt <= k and ptr:
            st.append(ptr.data)
            ptr = ptr.next
            cnt += 1
        while st:
            ele = st.pop()
            new_list.append(ele)
        if not ptr:
            break

    return new_list


def merge_two_sorted_linked_list(list1, list2):
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


def merge_sort_linked_list(ll, cnt):
    ptr = ll.head
    if not ptr:
        return ll
    if ptr.next is None:
        return ll
    lst1 = LinkedList()
    lst1.head = Node(ptr.data)
    ptr = ptr.next
    for i in range(1, cnt//2):
        lst1.append(ptr.data)
        ptr = ptr.next
    lst2 = LinkedList()
    lst2.head = Node(ptr.data)
    ptr = ptr.next
    for i in range(1, cnt-cnt//2):
        lst2.append(ptr.data)
        ptr = ptr.next
    lst1 = merge_sort_linked_list(lst1, cnt//2)
    lst2 = merge_sort_linked_list(lst2, cnt-cnt//2)
    ll = merge_two_sorted_linked_list(lst1, lst2)
    return ll


def add_two_number_as_ll(llist1, llist2):
    first = llist1.head
    second = llist2.head
    res = LinkedList()
    if not first and not second:
        return res
    carry = 0
    while first and second:
        num = carry + first.data + second.data
        if num > 9:
            carry = num // 10
            num = num % 10
        res.append(num)
        first = first.next
        second = second.next
    while first:
        num = first.data + carry
        if num > 9:
            carry = num // 10
            num = num % 10
        first = first.next

    while second:
        num = second.data + carry
        if num > 9:
            carry = num // 10
            num = num % 10
        res.append(num)
        second = second.next
    return res





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
    # Inseting two nodes in front
    llist.push(0)
    llist.push(-1)
    # Appending new node
    llist.append(4)
    llist.append(5)
    # Delete -1, 3
    llist.delete_by_key(-1)
    llist.delete_by_key(3)
    # Appending new node
    llist.append(6)
    llist.append(7)
    # Deleting element at 3rd postion
    llist.delete_by_position(1)
    # Length of linked list (recursively)
    print llist.length_recur()
    # Length of linked list iteratively
    print llist.length()
    # Swap node with data 2 and node with data 6
    llist.swap_nodes(1, 7)
    # Reverse a linked list
    # llist.reverse()
    # # Reverse a linked list recursively
    # llist.reverseRecur(llist.head)
    llist.display()
    # Merging two linked list
    # llist2 = LinkedList()
    # llist3 = LinkedList()
    # # Appending data in llist2
    # llist2.append(5)
    # llist2.append(10)
    # llist2.append(15)
    # # Display 2nd list
    # llist2.display()
    # # Appending data in llist3
    # llist3.head = Node(2)
    # llist3.append(3)
    # llist3.append(20)
    # # Display 3rd list
    # llist3.display()
    # merged = LinkedList()
    # merged = merge_two_sorted_linked_list(llist2, llist3)
    # merged.display()
    # llist = merge_sort_linked_list(llist, llist.length())
    # llist.display()
    list3 = LinkedList()
    for i in range(1, 10):
        list3.append(i)
    # list3 = merge_sort_linked_list(list3, list3.length())
    # list3.display()
    # list3 = LinkedList()
    # list3.head = Node(1)
    # list3.head.next = Node(2)
    # list3.head.next.next = Node(3)
    # list3.head.next.next.next = Node(4)
    # list3.head.next.next.next.next = Node(5)
    # list3.head.next.next.next.next.next = Node(6)
    # list3.head.next.next.next.next.next.next = list3.head.next.next
    # print list3.isLoop()
    # list3.display()
    # print list3.isLoopAndRemove()
    # list3.display()
    ## Reversing a linked list in size of k
    # list3.display()
    # list3 = reverse_group_of_size_k(list3, 3)
    # list3.display()
    # Rotate linked list anticlock wise by k
    list4 = LinkedList()
    for i in range(1, 7):
        list4.append(i)
    list4.rotate_by_k_anti_clock(1)
    list4.display() 
