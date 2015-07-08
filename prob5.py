import PE

def prob5():
	prod = 1
	for i in range(1,21):
		if PE.isPrime(i):
			prod *= i
		if prod % i != 0:
			k = i
			m = prod
			for c in range(1,i/2 + 1):
				if m % c == 0 and k % c == 0:
					k /= c
					m /= c
			prod *= k
	print(prod)


prob5()