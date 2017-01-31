
def merge(array, beg, mid, end):
	i = beg
	j = mid + 1
	B = []
	while i <= mid and j <= end:
		if array[i] < array[j]:
			B.append(array[i])
			i= i + 1
		else:
			B.append(array[j])
			j = j + 1
	while i <= mid:
		B.append(array[i])
		i = i + 1
	while j <= end:
		B.append(array[j])
		j = j + 1

	i = beg
	for v in B:
		array[i] = v
		i = i + 1

def merge_sort(array, beg, end):
	if beg >= end:
		return
	mid = (beg + end)/2
	merge_sort(array, beg, mid)
	merge_sort(array, mid + 1, end)
	merge(array, beg, mid, end)

# Tests
q = [5, 6 , 3, 1, 8, 9, 2, 4, 10]
s = [3, 1, 2]


print "Original Array"
print q

merge_sort(q, 0, len(q) - 1)

print "Sorted Array"
print q

print "Original Array"
print s

merge_sort(s, 0, len(s) - 1)

print "Sorted Array"
print s