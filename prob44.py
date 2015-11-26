

def prob44():
	n = 1
	l = set()
	while True:
		newterm = n*(3*n-1)/2
		l.add(newterm)
		print(newterm)
		for terma in l:
			for termb in l:
				if (terma + termb) in l and ((terma - termb) in l or (termb - terma) in l):
					return terma - termb
		
		n += 1

print(prob44())