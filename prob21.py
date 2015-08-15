import PE

def prob21():
	summ=0
	for i in range(1,10000):
		x = PE.sumDivisors(i)
		if x!= i and PE.sumDivisors(x) == i:
			summ += i
			print(i)
	print(summ)

prob21()