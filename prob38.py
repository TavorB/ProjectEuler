import PE

maxPan = 0
for i in range(1,10**5):
	for n in range(2,10):
		newNum = str(i)
		for count in range(2, n+1):
			if len(newNum) > 9:
				break
			newNum += str(i * count)
		if PE.pandigital(int(newNum)):
			maxPan = max(maxPan, int(newNum))
print(maxPan)