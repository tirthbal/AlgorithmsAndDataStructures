from stack_ll import Stack_ll


def reverse_string(original):
	result = ''
	st = Stack_ll()
	
	for c in original:
		st.push(c)
	
	while st.get_top():
		result += st.pop()

	return result


print reverse_string("abaracadabra")
print reverse_string("hello")



