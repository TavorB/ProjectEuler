import PE

def prob10():
	summ = 0
	for i in range(2,2000000):
		print(i)
		if PE.isPrime(i):
			summ += i
	print(summ)

prob10()