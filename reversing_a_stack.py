from stack import Stack


''' 
Input
5 4 3 1 2
Output
2 1 3 4 5
'''

def recur(st):
	if not st.get_top():
		return
	ele = st.pop()
	recur(st)
	st.push(ele)

st = Stack()
for i in [5, 4, 3, 1, 2]:
	st.push(i) 

recur(st)
while not st.get_top():
	print st.pop()