num = 3
den = 2
numgreater = 0

for _ in range(1,1000):
	print _
	if len(str(num)) > len(str(den)):
		numgreater +=1
	num, den = num + 2*den, num + den

print numgreater