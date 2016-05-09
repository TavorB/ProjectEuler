import PE

x = 1

while True:
	print x
	digitsArr = PE.numToDigitArr(x)
	digitsArr2 = PE.numToDigitArr(2*x)
	if digitsArr == digitsArr2:
		digitsArr3 = PE.numToDigitArr(3*x)
		if digitsArr == digitsArr3:
			digitsArr4 = PE.numToDigitArr(4*x)
			if digitsArr == digitsArr4:
				digitsArr5 = PE.numToDigitArr(5*x)
				if digitsArr == digitsArr5:
					digitsArr6 = PE.numToDigitArr(6*x)
					if digitsArr == digitsArr6:
						print x
						break
	x+=1