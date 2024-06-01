for i in range(1,101):
	print(*[n for n in range(1,i+1) if i%n==0])
