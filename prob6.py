
def prob6():
	a = 0
	for i in range(1,101):
		a += i*i
	b = 0
	for i in range(101):
		b += i
	b*=b
	print(b - a)

prob6()
