import sys
d={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1,' ':0}
for a in sys.argv[1:]:
 t=i=0;a+=' '
 while a[i]!=' ':
  p=d[a[i]];q=d[a[i+1]]
  if q>p:t+=q-p;i+=2
  else:t+=p;i+=1
 print(t)
