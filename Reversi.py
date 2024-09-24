import sys
z=print;h=(-1,0,1)
def w(x,y,i,j,b):
	f=0
	while -1<x<8and -1<y<8:
		c=b[y][x]
		if c=='X':f=1
		if c=='O':return f
		if c=='.':return 0
		x+=i;y+=j
	return 0
for a in sys.argv[1:]:
	a=a.split()
	for y in range(8):
		for x in range(8):
			c=a[y][x]
			z([c,'!'][c=='.'and any(w(x+i,y+j,i,j,a)for i in h for j in h)],end='')
		z()
	z()
