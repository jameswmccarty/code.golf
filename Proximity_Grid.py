import sys,string as s
c=s.digits+s.ascii_letters.swapcase()
r,z=range,print
def d(x,y,b):
	p,v,q=b[y][x],set(),[(x,y,0)]
	if p in'0#':return p
	while q:
		i,j,s=q.pop(0)
		if b[j][i]=='0':return c[s]
		for k,l in((0,1),(1,0),(-1,0),(0,-1)):
			m,n=i+k,j+l
			if 0<=n<9 and 0<=m<9 and b[n][m]!='#' and(m,n)not in v:q+=[(m,n,s+1)];v.add((m,n))
	return p
def t(b):
	for j in r(9):z(''.join(d(i,j,b.split('\n'))for i in r(9)))
for a in sys.argv[1:]:t(a);z()
