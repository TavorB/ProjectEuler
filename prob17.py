
counts = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tensplace = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
def prob17():
	ret = 0
	for i in range(1,1000):
		hundreds = int(i/100)
		tens = int((i%100) / 10)
		ones = i % 10
		wordstring=""
		if i >= 100:
			wordstring+= counts[hundreds] + "hundred"
			if i % 100 != 0:
				wordstring += "and"
		if tens == 1:
			wordstring+= teens[ones]
		else:
			wordstring+= tensplace[tens] + counts[ones]
		ret+= len(wordstring)
	print(ret + 11)

prob17()