r=range
for n in r(1,10001):
	e=[x for x in r(1,n+1)if n%x==0]
	a,b=sum(e),len(e)
	if a/b-a//b==0:print(n)
