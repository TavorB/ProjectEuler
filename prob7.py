import PE

def prob7():
	numprimes = 1
	i = 2
	while numprimes != 10001:
		print(i)
		print(numprimes)
		i += 1
		if PE.isPrime(i):
			numprimes += 1
		
	print("and it is")
	print(i)

prob7()