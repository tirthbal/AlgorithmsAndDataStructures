from stack_ll import Stack_ll


def sorted_insert(st, ele):
	if not st.get_top() or st.get_top() > ele:
		st.push(ele)
	else:
		tmp = st.pop()
		sorted_insert(st, ele)
		st.push(tmp)

def sort_stack(st):
	if not st.get_top():
		return
	tmp = st.pop()
	sort_stack(st)
	sorted_insert(st, tmp)


st = Stack_ll()

for i in [-3, 14, 18, -5, 30]:
	st.push(i)

sort_stack(st)

while st.get_top():
	print st.pop()