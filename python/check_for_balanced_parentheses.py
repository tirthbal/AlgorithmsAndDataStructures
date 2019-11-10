from stack_ll import Stack_ll


def check_for_balanced_parentheses(expr):
	st = Stack_ll()
	for c in expr:
		if c == '(' or c == '{' or c == '[':
			st.push(c)
			continue
		if c == ')' and st.get_top() == '(':
			st.pop()
			continue
		if c == '}' and st.get_top() == '{':
			st.pop()
			continue
		if c == ']' and st.get_top() == '[':
			st.pop()
			continue
		return False
	return True

print check_for_balanced_parentheses("[()]{}{[()()]()}")
print check_for_balanced_parentheses("(){}[]]")