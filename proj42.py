def wordToVal(strang):
	retval = 0
	for char in strang:
		retval += ord(char) - 64
	return retval + 60 #need to account for starting and ending "


f = file('p042_words.txt').read()
triangleNums = set()
for n in range(1,10000):
	triangleNums.add(n * (n+1) / 2)

numTriangles = 0
numWords = 0
for word in f.split(","):
	numWords +=1
	wordsum = wordToVal(word)
	if wordsum in triangleNums:
		numTriangles +=1

print(numTriangles)