

def printList(head):
	ptr = head
	if ptr != None:
		print ptr.data
		while True:
			ptr = ptr.next
			if ptr == head:
				break
			print ptr.data