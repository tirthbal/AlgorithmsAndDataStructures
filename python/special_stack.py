from stack_ll import Stack_ll


class SpecialStack():

	def __init__(self):
		self.ori_stack = Stack_ll()
		self.min_stack = Stack_ll()

	def get_top(self):
		return self.ori_stack.get_top()

	def isEmpty(self):
		return True if not self.ori_stack.get_top() else False

	def push(self, data):
		if self.isEmpty():
			self.ori_stack.push(data)
			self.min_stack.push(data)
		else:
			self.ori_stack.push(data)
			if self.min_stack.get_top() > data:
				self.min_stack.push(data)

	def pop(self):
		if self.isEmpty():
			return None
		ele = self.ori_stack.pop()
		if ele == self.min_stack.get_top():
			self.min_stack.pop()
		print 'Popping ' + str(ele) + ' from the stack.'
		return ele

	def get_min(self):
		if self.isEmpty():
			return None
		return self.min_stack.get_top()



if __name__ == '__main__':
	sp_st = SpecialStack()
	for i in [10, 20, 30]:
		sp_st.push(i)
	print 'Current minimum is ' + str(sp_st.get_min())
	sp_st.push(5)
	print 'Current minimum is '  + str(sp_st.get_min())
	sp_st.push(12)
	print 'Current minimum is ' + str(sp_st.get_min())
	sp_st.pop()
	sp_st.pop()
	print 'Current minimum is ' + str(sp_st.get_min())
