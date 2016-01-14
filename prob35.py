import PE

primes = 0
for i in range(2,1000000): #
	k = i
	circPrime = True
	if not PE.isPrime(i):
		continue
	for count in range(1, len(str(i))):
		k = int(str(i)[count:] + str(i)[:count])
		if not PE.isPrime(k):
			circPrime = False
			break
	if circPrime:
		primes +=1
print(primes)


