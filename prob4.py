import PE

def prob4():
	maxn = 0
	for i in range(999, 900 , -1):
		for j in range(999, 900 , -1):
			print(i, j)
			if i*j > maxn and PE.isPalindrome(i*j):
				maxn = i*j
	print(maxn)

prob4()