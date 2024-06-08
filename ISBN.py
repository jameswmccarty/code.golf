import sys
def d(s):
	t=(s[0]*10+sum((10-i)*s[i]for i in range(1,9)))%11
	t=(11-t)%11
	return'X'if t==10else str(t)
for a in sys.argv[1:]:
	print(a+d(list(map(int,a.replace('-','')))))
