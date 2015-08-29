import PE

def prob41():
	for n in range(10,3,-1):
		l = set()
		for i in range(1,n):
			l.add(i)
		k = prob41H("", l, set())
		if k != 0:
			return k

def prob41H(strang, arrToPut, arrIn):
	print(strang)
	# myarr = arr.copy()
	if len(strang) == len(arrToPut):
		if PE.isPrime(int(strang)):
			return int(strang)
		else:
			return 0
	l = set()
	l.add(0)
	for i in arrToPut:
		if i not in arrIn:
			newArrIn = arrIn.copy()
			newArrIn.add(i)
			# newArrToPut = arrToPut.copy()
			# newArrToPut.remove(i)
			l.add(prob41H(strang + str(i), arrToPut, newArrIn))
	print("l : " + str(l))
	return max(l)





	# l = set()
	# for dec in range(1000):
	# 	for i in range(987654321 - (2**15) * dec,987654321 - (2**15) * (dec + 1), -1):
	# 		print(i)
	# 		if PE.isPrime(i) and PE.nPandigital(i, len(str(i))):
	# 			print("done")
	# 			print(i)
	# 			return
	# for n in range(9,2,-1):
	# 	for i in range(10**(n), 10**(n-1), -1):
	# 		print(i)
	# 		if PE.nPandigital(i,n):
	# 			print(i)
	# 			return i

print(prob41())