import math
import PE

def prob47():
	i = 640
	while True:
		curr = set()
		print(i)
		for j in range(4):
			val = PE.factorize(i+j)
			if len(val) != 4:
				break
			# curr = curr.union(val)
			# if len(curr) != 3 * (j+1):
			# 	break
			if j==3:
				print("soln is: " + str(i))
				return
		i+=1

prob47()