import sys
for a in sys.argv[1:]:
 a=int(a,2);b=a
 while b:b=b>>1;a^=b
 print(a)
