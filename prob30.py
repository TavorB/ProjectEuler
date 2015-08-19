

def prob30():
	summ = 0
	for i in range(2,1000000):
		print(i)
		currsumm = 0
		for ind in range(len(str(i))):
			currsumm += int(str(i)[ind]) ** 5
		if currsumm == i:
			summ += i
	print(summ)

prob30()
