import math

def isPrime(k):
	for i in range(2, (int) (math.sqrt(k)) + 1):
		if k % i == 0:
			return False
	return True