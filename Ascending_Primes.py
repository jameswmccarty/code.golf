z,r=print,range
b=lambda x: len(set(str(x)))==len(str(x))and list(str(x))==sorted(list(str(x)))
p=lambda x:not any(x%i==0for i in r(2,x))
z('2')
for a in r(3,23456790,2):
	if b(a)and p(a):
		z(a)
