import PE

def prob23():
	summ = 0;
	S = set()
	for i in range(1,28124):
		if PE.sumDivisors(i) > i:
			S.add(i)
	for i in range(1, 28124):
		abundantsum = False
		for x in S:
			if (i - x) in S:
				abundantsum = True
				break
		if not abundantsum:
			print(i)
			summ += i
	return summ

print(prob23())