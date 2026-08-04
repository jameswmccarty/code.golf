import sys
d={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1,' ':0}
for a in sys.argv[1:]:
 t=i=0;a=a[::-1]+' '
 while i<len(a)-1:
  if d[a[i+1]]<d[a[i]]:t+=d[a[i]]-d[a[i+1]];i+=2
  else:t+=d[a[i]];i+=1
 print(t)
