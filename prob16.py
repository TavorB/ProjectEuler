

def prob16():
	k = str(2 ** 1000)
	numarr = list(k) 
	currsum = 0
	for i in range(len(numarr)):
		currsum += int(numarr[i])
	print(currsum)

prob16()