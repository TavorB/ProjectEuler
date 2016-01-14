import math

def factorial(k):
	if k<=1:
		return 1
	return k * factorial(k-1)

def isPrime(k):
	if k <= 1:
		return False
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

def nPandigital(a, n):
	if len(str(a)) != n:
		return False
	l = set()
	while a:
		if a%10 != 0:
			l.add(a%10)
		a /= 10
	return len(l) == n

def pandigital(a):
	return nPandigital(a, 9)

def factorize(n):
	ret = set()
	while n != 1:
		k = n
		for i in range(2,int(math.sqrt(n)) + 1):
			if n % i ==0:
				ret.add(i)
				n /= i
				break
		if k == n:
			ret.add(n)
			break
	return ret

def choose(n,c):
	return factorial(n)/factorial(c)/factorial(n-c)
	
def isPermutation(a,b):
	first = dict()
	second = dict()
	while a > 0:
		digit = a%10
		if digit in first:
			first[digit] += 1
		else:
			first[digit] = 1
		a /= 10
	while b > 0:
		digit = b%10
		if digit in second:
			second[digit] += 1
		else:
			second[digit] = 1
		b /= 10
	return first == second
