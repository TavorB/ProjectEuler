import PE

def prob3():
	num = 600851475143
	curr = 1
	maxnum = 0
	while(curr < num):
		if num % curr == 0:
			num /= curr
			if PE.isPrime(num):
				maxnum = num
		print(curr)
		curr += 1
	print("and the result is")
	print(maxnum)
	return maxnum

prob3()