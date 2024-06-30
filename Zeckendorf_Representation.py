import sys
def b(n):
	f=[1,1]
	while f[-1]<=n:f+=[sum(f[-2:])]
	return f[::-1][1:]
d=n=0
def s(a,b):
	global d,n
	if d:return
	if sum(b)==n:print(' + '.join(str(x)for x in b));d=1
	if a and sum(b)<n:s(a[2:],b+[a[0]]);s(a[1:],b)
for g in sys.argv[1:]:
	d,n=0,int(g);s(b(n),[])
