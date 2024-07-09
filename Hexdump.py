import sys
def p(a):
	i=0
	while a:
		w=a[:16];a=a[16:];l=[' ']*40;j=0;u=-1
		for v in ''.join(hex(ord(c))[2:].zfill(2)for c in w):
			u+=1
			if u==4:j+=1;u=0
			l[j]=v;j+=1
		print(hex(i)[2:].zfill(8)+':',''.join(l),w.replace('\n','.'))
		i+=16
	print()
for a in sys.argv[1:]:p(a)
