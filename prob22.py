

def wordToVal(strang):
	retval = 0
	for char in strang:
		retval += ord(char) - 64
	return retval + 60 #need to account for starting and ending "

f = file('p022_names.txt').read()
arr = f.split(",")
arr = sorted(arr)

i = 1
summ = 0
for word in arr:
	summ += i * wordToVal(word)

	i+=1
print(summ)


