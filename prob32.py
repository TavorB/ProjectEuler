
def prob32():
	summ = set()
	for a in range(1,10 ** 3):
		# print(a)
		# for b in range(10 ** (10 - 2 * len(str(a))),10 ** (11 - 2 * len(str(a)))):
		# for b in range(10 ** (5 - len(str(a))),
		for b in range(10 ** (4 - len(str(a))), 10 ** (5 - len(str(a)))):
			if len(str(a)) + len(str(b)) + len(str(a*b)) > 9:
				break;
			if (pandigital(a,b,a*b)):
				summ.add(a*b)
	print(reduce(lambda x, y: x+y, summ))

def pandigital(a,b,c):
	if len(str(a)) + len(str(b)) + len(str(c)) != 9:
		return False
	l = set()
	while a:
		l.add(a%10)
		a /= 10
	while b:
		l.add(b%10)
		b /= 10
	while c:
		l.add(c%10)
		c /= 10
	l.add(0)
	return len(l) == 10

# print(pandigital(39, 186, 7254))
prob32()