from queue_ll import Queue


def binary_generator(n):
	qu = Queue()
	qu.enqueue('1')
	count = 0
	while count < n:
		num = qu.dequeue()
		print num
		count += 1
		qu.enqueue(num + '0')
		qu.enqueue(num + '1')


if __name__ == '__main__':
	binary_generator(5)