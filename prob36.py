import PE

summ = 0
for i in range(1,1000000):
	if PE.isPalindrome(i) and PE.isPalindrome(bin(i)[2:]):
		print(i)
		summ += i
print(summ)
