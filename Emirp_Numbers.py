r,s=range,str
p=lambda x:not any(x%i==0 for i in r(2,x))
for a in r(2,1001):
	if (s(a)[::-1]!=s(a))&p(a)&p(int(s(a)[::-1])):
		print(a)
