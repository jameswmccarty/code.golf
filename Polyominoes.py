z,r,m,M=print,range,min,max
def n(p):
	p={(x-m(p[0]for p in p),y-m(p[1]for p in p))for x,y in p};i=j=1
	if(1,0)in p:j=0
	if(0,0)in p:i=0
	return{(x-i,y-j)for x,y in p}
def g():
	q,p,t=[],{(0,0)},set()
	q+=[p]
	while q:
		s=q.pop(0);t.add(frozenset(n(s)))
		for p in s:
			x,y=p
			for i,j in((0,1),(1,0),(-1,0),(0,-1)):
				if(x+i,y+j)not in s and len(s)<6:q+=[{*s,(x+i,y+j)}]
	return t
for s in g():
	d,e=[p[0]for p in s],[p[1]for p in s]
	for y in r(m(e),M(e)+1):
		for x in r(m(d),M(d)+1):
			z(' #'[(x,y)in s],end='')
		z()
	z()
