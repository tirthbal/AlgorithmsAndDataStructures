

class BinHeap:

	def __init__(self):
		self.heapList = [0]
		self.current_size = 0

	def prec__up(self, pos):
		parent = pos // 2
		child = pos
		while self.heapList[parent] > self.heapList[child] and child != parent and parent > 0:
			self.heapList[parent], self.heapList[child] = self.heapList[child], self.heapList[parent]
			child = parent
			parent = child // 2

	def perc_down(self, pos):
		parent = pos
		child = self.min_child(pos)
		while child <= self.current_size and self.heapList[parent] > self.heapList[child]:
			self.heapList[parent], self.heapList[child] = self.heapList[child], self.heapList[parent]
			parent = child
			child = self.min_child(parent)

	def min_child(self, pos):
		if 2 * pos + 1 > self.current_size:
			return 2*pos
		else:
			if self.heapList[2 * pos] < self.heapList[2 * pos + 1]:
				return 2 * pos
			else:
				return 2 * pos + 1

	def insert(self, data):
		self.heapList.append(data)
		self.current_size += 1
		self.prec__up(self.current_size)

	def del_min(self):
		if not self.current_size:
			return 0
		ele = self.heapList[1]
		self.heapList[1] = self.heapList[self.current_size]
		self.heapList.pop()
		self.current_size -= 1
		self.perc_down(1)
		return ele

	def build_heap(self, alist):
		 i = len(alist) // 2
		 self.current_size = len(alist)
		 self.heapList = [0] + alist[:]
		 while i > 0:
		 	self.perc_down(i)
		 	i = i - 1


if __name__ == '__main__':
	alist = [9, 5, 6, 2, 3]
	bin_heap = BinHeap()
	bin_heap.build_heap(alist)
	while True:
		val = bin_heap.del_min()
		if not val:
			break
		print val,



