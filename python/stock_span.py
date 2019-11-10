from stack_ll import Stack_ll


def stock_span(prices):
	span = []
	st = Stack_ll()
	for price in prices:
		cnt = 0
		while st.get_top() and st.get_top()[0] <= price :
			cnt += st.get_top()[1]
			st.pop()
		cnt += 1
		span.append(cnt)
		st.push((price, cnt))
	return span


prices = [100, 80, 60, 70, 60, 75, 85]

print stock_span(prices)

prices = [10, 4, 5, 90, 120, 80]

print stock_span(prices)