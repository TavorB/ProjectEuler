

def Collatz(k):
	i = 1
	while k > 1:
		if k%2 == 0:
			k /= 2
		else:
			k = 3 * k + 1
		i+=1
	return i

def prob14():
	maxnum = 0
	maxcount = 0
	for i in range(1000000):
		print(i)
		curr = Collatz(i)
		if curr > maxcount:
			maxcount, maxnum = curr, i
	print(maxnum)

prob14()