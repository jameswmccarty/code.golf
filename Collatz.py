c=lambda n: n-1 if n<=1 else(1+c(3*n+1) if n&1 else 1+c(n//2))
for i in range(1,1001):
	print(c(i))
