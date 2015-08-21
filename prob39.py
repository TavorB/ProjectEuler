import PE, math

def prob39():
	maxP = 0
	maxCount = 0
	for p in range(1,1000):
		print(p)
		currcount = 0
		for a in range(1,p/2):
			for b in range(1,p-2*a):
				c = math.sqrt(a*a + b*b)
				if int(c) == c and a+b+c == p:
					currcount +=1
		if currcount > maxCount:
			maxCount, maxP = currcount, p
	return maxP
print(prob39())