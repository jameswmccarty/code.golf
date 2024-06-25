import sys
w=set()
m=M=0
t,r,k=enumerate,range,print
for y,l in t(sys.argv[1].split('\n')):
	for x,c in t(l):
		p=(x,y);m=len(l)
		if c=='S':s=p
		if c=='E':e=p
		if c=='#':w.add(p)
M=y
def b(v):
	for y in r(M+1):
		for x in r(m+1):
			g,c=(x,y),' '
			if g in v:c='.'
			if g in w:c='#'
			if g==s:c='S'
			if g==e:c='E'
			k(c,end='')
		k()
q=[(s,set())]
v=set()
while q:
	c,o=q.pop(0)
	if c==e:b(o);break
	for i,j in((0,1),(0,-1),(-1,0),(1,0)):
		a=(c[0]+i,c[1]+j)
		if a not in w and a not in v:q+=[((a,{*o,a}))];v.add(a)
