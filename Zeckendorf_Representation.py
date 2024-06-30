import sys
def b(n):
	f=[1,1]
	while f[-1]<=n:f+=[sum(f[-2:])]
	return f[::-1][1:]
d=0
def s(n,a,b):
	global d
	if d:return
	if sum(b)==n:print(' + '.join(str(x)for x in b));d=1
	if a and sum(b)<n:s(n,a[2:],b+[a[0]]);s(n,a[1:],b)
for g in sys.argv[1:]:
	d,g=0,int(g);s(g,b(g),[])
