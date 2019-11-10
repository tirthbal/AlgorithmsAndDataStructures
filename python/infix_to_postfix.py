from stack_ll import Stack_ll


# (a + b * c) --> Infix
# abc*+ -> Postfix


def get_priority(op):
	if op == '^':
		return 4
	if op == '*' or op == '/':
		return 3
	if op == '+' or op == '-':
		return 2
	if op == '(' or op == ')':
		return 1
	return -1


def infix_to_postfix(expr):
	expr += ')'
	st = Stack_ll()
	ans = ''
	st.push('(')
	for c in expr:
		if not c.isalpha():
			if c == ')':
				while st.get_top() != '(' and st.get_top():
					ans += st.pop()
				st.pop()
			elif c == '(':
				st.push(c)
			else:
				while get_priority(c) <= get_priority(st.get_top()) and st.get_top != '(':
					ans += st.pop()
				st.push(c)

		else:
			ans += c
	return ans

print infix_to_postfix("a+b*(c^d-e)^(f+g*h)-i")



