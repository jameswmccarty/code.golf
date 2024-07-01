import sys
f=[1,1]
while f[0]<2**31:f=[f[0]+f[1]]+f
d=n=0
def s(a,b):
	global d
	if d:return
	if sum(b)==n:print(' + '.join(str(x)for x in b));d=1
	if a and sum(b)<n:s(a[2:],b+[a[0]]);s(a[1:],b)
for g in sys.argv[1:]:d,n=0,int(g);s(f,[])
