import PE

count = 0
for n in range(23,101):
	for r in range(n):
		if PE.choose(n,r) > 1000000:
			count +=1
print(count)