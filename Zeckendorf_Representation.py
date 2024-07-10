import sys
f=[1,1]
while f[0]<2**31:f=[f[0]+f[1]]+f
def s(a,b):
	global d
	if d:
		if sum(b)==n:print(' + '.join(map(str,b)));d=0
		if a and sum(b)<n:s(a[2:],b+[a[0]]);s(a[1:],b)
for g in sys.argv[1:]:d,n=1,int(g);s(f,[])
