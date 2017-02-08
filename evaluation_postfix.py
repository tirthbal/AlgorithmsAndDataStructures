from stack_ll import Stack_ll

# 2 3 1 * + 9 -


def cal(a, b, op):
	if op == '^':
		return a ^ b
	if op == '*':
		return a * b
	if op == '/':
		return a / b
	if op == '+':
		return a + b
	if op == '-':
		return a - b


def evaluation_postfix(expr):
	st = Stack_ll()

	for c in expr:
		if not c.isdigit():
			b = st.pop()
			a = st.pop()
			st.push(cal(a, b, c))
		else:
			st.push(int(c))
	return st.pop()

print evaluation_postfix("231*+9-")
