maxsum = 0
maxa = 0
maxb = 0
for a in range(1,101):
	for b in range(1,101):
		mynum = a ** b
		summ = 0
		for ch in str(mynum):
			summ += int(ch)
		if summ > maxsum:
			maxsum = summ
			maxa = a
			maxb = b
		print str(a) + " ** " + str(b) + " => " + str(summ)
print str(maxa) + " ** " + str(maxb) + " => " + str(maxsum)