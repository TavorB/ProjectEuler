

dec = 1
prod = 1
nextval = 1
for i in range(1,1000000):
	if dec > 1000000:
		break
	if dec + len(str(i)) > nextval:
		prod *= int(str(i)[nextval-dec])
		nextval *=10
	dec+=len(str(i))
print(prod)