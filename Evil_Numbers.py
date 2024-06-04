for i in range(1001):
	if not bin(i).count('1')&1:
		print(i)
