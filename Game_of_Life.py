import sys
l,z,g,q=set(),print,range,(-1,0,1)
j=0
for r in sys.argv[1].split():
	i=0
	for c in r:
		if c=='#':l.add((i,j))
		i+=1
	j+=1
c=lambda x,y:sum((x+a,y+b)in l and(a,b)!=(0,0)for a in q for b in q)
for j in g(32):
	for i in g(32):
		v=c(i,j)
		if ((i,j)in l and v in(2,3)) or ((i,j)not in l and v==3):z('#',end='')
		else:z('.',end='')
	z()
