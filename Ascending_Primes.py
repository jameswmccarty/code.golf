l,s,t,r,q,o=len,set,list,range,print,str
b=lambda x:l(s(o(x)))==l(o(x))and t(o(x))==sorted(t(str(x)))
p=lambda x:not any(x%i==0 for i in r(2,x))
q('2')
for a in r(3,23456790,2):
	if b(a)and p(a):
		q(a)
