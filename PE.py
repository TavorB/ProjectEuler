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



def stringToArr(strIn,row,col):
	toArr = strIn.split(" ");
	retArr = []

	for y in range(row):
		currRow = []
		for x in range(col):
			currnum = int(toArr[col * y + x])
			
			currRow.append(currnum)
		retArr.append(currRow)
	return retArr



def numDivisors(num):
	k=0
	for i in range(1,int(math.sqrt(num)) + 1):
		if num % i == 0:
			k += 2
	if int(math.sqrt(num)) == math.sqrt(num):
		k-=1
	return k


def nthNatural(n):
	summ = 0
	for i in range(n + 1):
		summ += i
	return summ

def sumDivisors(n):
	k=0
	for i in range(1,int(math.sqrt(n)) + 1):
		if n % i == 0:
			k += i + n / i
	if int(math.sqrt(n)) == math.sqrt(n):
		k-= math.sqrt(n)
	return k - n