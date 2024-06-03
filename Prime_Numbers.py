r=range
p=lambda x:not any(x%i==0 for i in r(2,x))
for a in r(2,10001):
	if p(a):
		print(a)
