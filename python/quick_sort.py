

def partition(array, pivot):
	ele = array[pivot]
	part = pivot
	for i in range(pivot, len(array)):
		if array[i] < ele:
			part += 1
			array[part], array[i] = array[i], array[part]
	array[pivot], array[part] = array[part], array[pivot]
	return part


def quick_sort(array, beg, end):
	if beg < end :
		p = partition(array, beg)
		quick_sort(array, beg, p - 1)
		quick_sort(array, p + 1, end)


# Tests
q = [5, 6 , 3, 1, 8, 9, 2, 4, 10]
s = [3, 1, 2]


print "Original Array"
print q

quick_sort(q, 0, len(q) - 1)

print "Sorted Array"
print q
