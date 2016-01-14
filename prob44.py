

l = set()

# for n in range(1,10000):
# 	l.add(n*(3*n-1)/2)

n = 1
while True:
	newterm = n*(3*n-1)/2
	l.add(newterm)
	# print(newterm)
	for terma in l:
		termb = newterm - terma
		if termb in l:
			dif = abs(termb-terma)
			if dif in l:
				print("found pair " + str(terma) + ", " + str(termb))
				print("dif is: " + str(dif))


		# for termb in l:
		# 	if (terma + termb) in l and ((terma - termb) in l or (termb - terma) in l):
		# 		return terma - termb
	
	n += 1