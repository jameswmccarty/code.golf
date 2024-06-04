r,s=range,str
p=lambda x:not any(x%i==0 for i in r(2,x))
for a in r(2,10001):
	b=s(a)[::-1]
	if (b!=s(a))&p(a)&p(int(b)):
		print(a)
