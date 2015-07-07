import math

def isPrime(int k):
	for i in range(math.sqrt(k) + 1):
		if k % i == 0:
			return false
	return true