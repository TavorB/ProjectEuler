import math

def isPrime(k):
	for i in range(2, (int) (math.sqrt(k)) + 1):
		if k % i == 0:
			return False
	return True

def isPalindrome(k):
	if k < 10:
		return True
	s = str(k)
	a,b = 0, len(s) - 1
	while a < b:
		if s[a] != s[b]:
			return False
		a,b = a + 1, b - 1
	return True
