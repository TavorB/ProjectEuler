import PE


def prob12():
	i = 1
	triangle = 0
	maxdiv = 0

	while True:
		triangle += i
		print(i)
		numdiv = PE.numDivisors(triangle)
		print(str(triangle) + " : " + str(numdiv))

		if numdiv >= 500:
			print(str(i) )
			return i
		i+=1

	# prod = 1
	# for i in range(1,500):
	# 	prod *= i
	# print(PE.nthNatural(500))
	# for i in range(8):
	# 	print(str(i) + " : " + str(PE.nthNatural(i)) +" : " + str(PE.numDivisors(PE.nthNatural(i))))
	# print(PE.numDivisors(25))

prob12()


# 6322445026 : 8
# 112450