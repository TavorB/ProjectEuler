import PE
numLychel = 0
for num in range(1, 10000):
	isPalindrome = False
	iterNum = num
	for iters in range(50):
		iterNum += PE.reverse(iterNum)
		if PE.isPalindrome(iterNum):
			isPalindrome = True
			break
	numLychel += 0 if isPalindrome else 1
print numLychel
