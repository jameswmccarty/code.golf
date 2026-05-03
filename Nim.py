import sys
for a in sys.argv[1:]:
 a=[*map(int,a.split())];s=i=0
 for p in a:s^=p
 for p in a:
  if p^s<=p:print(i,p-(p^s))
  i+=1
