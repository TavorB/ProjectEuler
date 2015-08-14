
def prob20():
	i = 1

	for n in range(1, 101):
		i *= n

	count = 0
	while i > 0:
		count += i % 10
		i /= 10
	print(count)

prob20()