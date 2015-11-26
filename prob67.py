

f = open('p067_triangle.txt', 'r')
triangle = ''
for line in f:
	triangle += line + " "

def triangleToArr(strIn):
	toArr = strIn.split(" ");
	toArr[:] = [x for x in toArr if x != '\n']
	retArr = []
	i = 0
	for y in range(1, 101):
		currRow = []
		for x in range(y):
			currnum = int(toArr[i])
			i+=1
			currRow.append(currnum)
		retArr.append(currRow)
	return retArr

def prob67():
	arr = triangleToArr(triangle)
	for x in range(1, 100):
		currRow = []
		for y in range(x + 1):
			if y==0:
				arr[x][y] += arr[x-1][y]
			elif y==x:
				arr[x][y] += arr[x-1][y-1]
			else:
				arr[x][y] += max(arr[x-1][y], arr[x-1][y-1])
	print(max(arr[99]))
prob67()