import PE

def prob27():
	maxcount = 0
	maxA = 0
	maxB = 0
	for a in range(-999,1000):
		for b in range(-999,1000):
			n=0
			while PE.isPrime(n*n + a*n+b):
				n +=1
			if n > maxcount:
				maxcount, maxA, maxB = n, a, b
			print(str(a) + ", " + str(b) + " : " + str(n))
	print(maxA)
	print(maxB)
	print(maxcount)
	print(maxA*maxB)

prob27()