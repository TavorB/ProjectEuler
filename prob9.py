import math



def prob9():
	for a in range(2,750):
		for b in range(2,750):
			print("a: " + str(a) + " b: " + str(b))
			if a + b + math.sqrt(a*a + b*b) == 1000:
				print(a*b*math.sqrt(a*a + b*b))
				return a*b*math.sqrt(a*a + b*b)

prob9()