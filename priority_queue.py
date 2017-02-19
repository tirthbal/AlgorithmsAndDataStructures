class Node:
	def __init__(self, item=None, priority=None):
		self.item = item
		self.priority = priority



class PriorityQueue:

	def __init__(self):
		self.heapList = [Node()]
		self.current_size = 0

	def highest_priority_child(self, pos):
		if 2 * pos + 1 > self.current_size:
			return 2 * pos
		if self.heapList[2 * pos].priority > self.heapList[2 * pos + 1].priority:
			return 2 * pos
		return 2 * pos + 1

	def prec_up(self, pos):
		child = pos
		parent = pos // 2
		while self.heapList[child].priority > self.heapList[parent].priority and parent > 0:
			self.heapList[child], self.heapList[parent] = self.heapList[parent], self.heapList[child]
			child = parent
			parent = child // 2

	def prec_down(self, pos):
		parent = pos
		child = self.highest_priority_child(pos)
		while child <= self.current_size and self.heapList[parent].priority < self.heapList[child].priority:
			self.heapList[child], self.heapList[parent] = self.heapList[parent], self.heapList[child]
			parent = child
			child = self.highest_priority_child(parent)

	def insert(self, node):
		self.heapList.append(node)
		self.current_size += 1
		self.prec_up(self.current_size)

	def get_highest_priority(self):
		if not self.current_size:
			return None
		return self.heapList[1].item

	def del_highest_priority(self):
		if not self.current_size:
			return None
		ele = self.get_highest_priority()
		self.heapList[1] = self.heapList[self.current_size]
		self.current_size -= 1
		self.heapList.pop()
		self.prec_down(1)
		return ele


if __name__ == '__main__':
	pq = PriorityQueue()
	for i, j in enumerate([10, 2, 31, 4, 51, 6]):
		new_node = Node(j, i)
		pq.insert(new_node)

	while pq.get_highest_priority():
		print pq.del_highest_priority(),


