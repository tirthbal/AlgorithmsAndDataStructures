


def cover_all_petrol_pump(alist):
	# alist : List of tuples e.g [(a, b), (c, d)]
	# (a, b) : a is petrol in litre , b is distance b/w this and next petrol pump
	front = 0
	rear = 0
	cur_capablity = (alist[0][0] - alist[0][1]) 
	for i in range(1, len(alist)):
		if cur_capablity < 0:
			front = i
			rear = i
			cur_capablity = (alist[i][0] - alist[i][1])
			continue
		cur_capablity += (alist[i][0] - alist[i][1])
		rear = i
	return front


if __name__ == '__main__':
	alist = [(4, 6), (6, 5), (7,3), (4,5)]
	print cover_all_petrol_pump(alist) + 1 
