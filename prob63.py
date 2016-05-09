import math

powerful = 0 

for power in range(1,10000):
	if power % 1000 == 0:
		print power	
	for val in range(1,10):
		num = val ** power
		if len(str(num)) == power:
			powerful += 1
		if len(str(num)) > power:
			break

print powerful