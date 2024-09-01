import sys
for a in sys.argv[1:]:
	x=0;b=a
	while b!=b[::-1]:b=a+a[0:x][::-1];x+=1
	print(b)
