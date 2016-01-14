import PE



for start in range(1, 9997):
	for increment in range(1, 3333):
		first = start
		second = start + increment
		third = start + 2*increment
		if third > 9999:
			continue
		if not (PE.isPermutation(first, second) and PE.isPermutation(first, third)):
			continue
		if not all(map(PE.isPrime, [first, second, third])):
			continue
		print(str(first) + str(second) + str(third))


# print(PE.isPermutation(1447, 4417))