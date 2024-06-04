z,r=print,range
b=lambda x,y:len({*y})==len(y)and [*y]==sorted([*y])
p=lambda x:not any(x%i==0for i in r(2,x))
z('2')
for a in r(3,23456790,2):
	if b(a,str(a))and p(a):
		z(a)
