
# op   main_stack   mid_stack
# pu 1	   1            1
# pu 2       1,2        1
# pu 3       1,2,3      1,2
# pu 7       1,2,3,7    1,2
# pu 8       1,2,3,7,8  1,2,3
# pop        1,2,3,7    1,2
from double_linked_list import DoubleLinkedList, Node


class MiddleStack:

	def __init__(self):
		self.top = DoubleLinkedList()
		self.mid = Node()
		self.count = 0

	def push(self, data):
		self.top.insert_at_beg(data)
		self.count += 1
		if self.count == 1:
			self.mid = self.top.head
		else:
			if self.count and self.count % 2 !=0 :
				self.mid = self.mid.prev

	def pop(self):
		if self.count == 0:
			print 'Stack is empty'
			return
		ele = self.top.head.data
		self.top.delete_head()
		self.count -= 1
		if self.count % 2 == 0:
			self.mid = self.mid.next
		return ele

	def findMiddle(self):
		return self.mid.data

	def get_top(self):
		return self.top.head.data

if __name__ == '__main__':
	ms = MiddleStack()
	for i in [11, 22, 33, 44, 55, 66, 77]:
		ms.push(i)
	print ms.pop()
	print ms.pop()
	print ms.findMiddle()
