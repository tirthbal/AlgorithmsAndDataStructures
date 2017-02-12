from stack_ll import Stack_ll


''' 
Input
5 4 3 1 2
Output
2 1 3 4 5
'''
rev_stack = Stack_ll()
def recur(st):
	if not st.get_top():
		return
	ele = st.pop()
	rev_stack.push(ele)
	recur(st)

st = Stack_ll()
for i in [5, 4, 3, 1, 2]:
	st.push(i) 

recur(st)

while rev_stack.get_top():
	print rev_stack.pop()