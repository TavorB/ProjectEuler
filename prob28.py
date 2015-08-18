
def prob28():
	summ = 1
	for i in range(1, (1001+1)/2):
		n = 2*i +1
		summ += 4*n*n - 6*(n -1)
	print(summ)

prob28()