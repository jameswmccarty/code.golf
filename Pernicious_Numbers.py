r,p,n=range,lambda x:x>1and not any(x%i==0 for i in r(2,x)),lambda x:p(bin(x).count('1'))
for i in r(51):
	if n(i):
		print(i)
