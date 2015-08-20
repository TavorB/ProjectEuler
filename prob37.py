import PE

def prob37():
	num = 0
	summ = 0
	i = 10
	while num < 11:
		# print(i)
		i += 1
		k = i
		works = True
		while k:
			if not PE.isPrime(k):
				works = False
				break
			k /= 10
		if works:	
			k = i
			while k:
				if not PE.isPrime(k):
					works = False
					break
				if k < 10:
					k = 0
				else :
					k = int(str(k)[1:])
		if works:
			print(i)
			num += 1
			summ += i
	print(summ)
prob37()