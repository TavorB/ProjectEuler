import PE

def prob34():
	summ = 0
	for i in range(3,1000000):
		print(i)
		k=i
		currsum = 0
		while k:
			currsum += PE.factorial(k%10)
			k/=10
		if currsum == i:
			summ += i
	print(summ)

prob34()