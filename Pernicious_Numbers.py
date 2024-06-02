p=lambda x:x>1 and not any(x%i==0 for i in range(2,x))
n=lambda x:p(bin(x).count('1'))
for i in range(51):
	if n(i):
		print(i)
