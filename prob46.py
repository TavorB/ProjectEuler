import PE
import math


def prob46():
	n = 3
	while True:
		print(n)
		if PE.isPrime(n):
			n+=2
			continue
		found = False
		for p in range(int(math.sqrt(n)) + 1):
			if PE.isPrime(n - 2*p*p):
				found = True
				break
		if not found:
			print("soln is: " + str(n))
			return
		n+=2

prob46()

