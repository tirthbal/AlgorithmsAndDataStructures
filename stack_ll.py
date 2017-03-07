from linked_list import LinkedList


class Stack_ll:

	# constructor for stack as linked list
	def __init__(self):
		self.top = LinkedList()

	# push into the stack
	def push(self, data):
		self.top.push(data)


	# pop from the stack
	def pop(self):
		return self.top.delete_beg()

	
	# get the top of the stack
	def get_top(self):
		if not self.top.head:
			return None
		return self.top.head


if __name__ == '__main__':
	st = Stack_ll()
	for i in [3, 2, 1, 4, 5]:
		st.push(i)
	while True:
		data = st.pop()
		if not data:
			break
		print data


