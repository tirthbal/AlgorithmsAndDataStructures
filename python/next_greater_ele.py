from stack_ll import Stack_ll
from collections import defaultdict

def next_greater_ele(array):
	st = Stack_ll()
	st.push(-1)
	ans = defaultdict()
	for i in reversed(array):
		while st.get_top() < i and st.get_top() != -1:
			st.pop()
		ans[str(i)] = st.get_top()
		st.push(i)
	return ans

array1 = [4, 5, 2, 25]
print next_greater_ele(array1)

array2 = [13, 7, 6, 12, 1]
print next_greater_ele(array2)

