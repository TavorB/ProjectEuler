nextarr = {1 : 2, 2 : 5, 5 : 10, 10 : 20, 20 : 50, 50 : 100, 100 : 200, 200 : -1}


def prob31(amount, coinlevel):
	if amount == 0 :
		return 1
	if amount < 0 or coinlevel == -1:
		return 0
	return prob31(amount - coinlevel, coinlevel) + prob31(amount, nextarr[coinlevel])

print(prob31(200, 1))