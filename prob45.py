import math

def prob45():
	n = 286;
	while True:
		print(n)
		curr = n*(n+1)/2.0
		pentRoot = int((1 + math.sqrt(24*curr)) / 6.0)
		if curr != pentRoot * (3 * pentRoot - 1) / 2.0 and curr != (pentRoot+1) * (3 * pentRoot + 2) / 2.0:
			n+=1
			continue
		hexRoot = int((1 + math.sqrt(1 + 8*curr)) / 4.0)
		if curr != hexRoot*(2*hexRoot - 1) and curr != (hexRoot + 1) * (2 * hexRoot + 1):
			n+=1
			continue
		print(str(n) + ", " + str(pentRoot) + ", " + str(hexRoot))
		print("sol: " + str(curr))
		return curr


prob45()