r=range
s=sorted
e=lambda x:str(x)[-1]=='0'
l=(9,100)
h=(101,1000)
v=lambda a,b:s(str(a*b))==s(str(a)+str(b))and not(e(a)&e(b))
p={a*b for a in r(*l)for b in r(*l)if v(a,b)}
f={a*b for a in r(*h)for b in r(*h)if v(a,b)}
for n in s({*p,*f}):print(n)
