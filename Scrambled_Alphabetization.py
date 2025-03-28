import sys,functools as f
def b(x,y):
 j,g,h=0,len(x),len(y)
 while j<min(g,h):
  p,q,j=k.index(x[j]),k.index(y[j]),j+1
  if p!=q:return [-1,1][q<p]
 return 0if x==y else [-1,1][g>h]
for a in sys.argv[1:]:k,*a=a.split();print(*sorted(a,key=f.cmp_to_key(b)))
