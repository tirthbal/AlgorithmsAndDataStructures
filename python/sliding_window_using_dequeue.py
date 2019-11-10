from dequeue import Dequeue

'''
arr[] = {1,2,3,1,4,5,2,3,6}
k = 3
o/p 3, 3, 4, 5, 5, 6

8, 5, 10, 7, 9, 4, 3, 2, 1, 0, 1
k = 4
o/p 10, 10, 10, 9, 9, 4, 3, 2
'''
def sliding_window(alist, window_size):
	dq = Dequeue()
	ans = []
	for i in range(0, window_size):
		if not dq.get_front():
			dq.insert_end((alist[i], i))
		elif alist[i] >= dq.get_end()[0]:
			dq.delete_end()
			dq.insert_end((alist[i], i))
		elif alist[i] >= dq.get_front()[0]:
			dq.delete_front()
			dq.insert_front((alist[i], i))
		else:
			dq.insert_front((alist[i], i))

	ans.append(dq.get_end()[0])
	for i in range(window_size, len(alist)):
		while (i - dq.get_end()[1]) >= window_size:
			dq.delete_end()
		if alist[i] >= dq.get_end()[0]:
			dq.delete_end()
			dq.insert_end((alist[i], i))
		elif alist[i] >= dq.get_front()[0]:
			dq.delete_front()
			dq.insert_front((alist[i], i))
		else:
			dq.insert_front((alist[i], i))
		ans.append(dq.get_end()[0])
	return ans

if __name__ == '__main__':
	alist = [1,2,3,1,4,5,2,3,6]
	print sliding_window(alist, 3)

	alist = [8, 5, 10, 7, 9, 4, 3, 2, 1, 0, 1]
	print sliding_window(alist, 4)



