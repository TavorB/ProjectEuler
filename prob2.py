def countevenfib():
	sum = 0
	a = 1
	b = 2

	while (b < 4000000):
		if b % 2 == 0:
			sum+= b
		a,b = b, a + b
	return sum
