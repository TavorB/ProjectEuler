import math


currsum = 0
for i in range(1,1001):
	print(i)
	currsum+= i**i
print("total: " + str(currsum))