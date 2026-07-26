import sys
from collections import defaultdict as d
q,p=range,print
h=[0,-1,1,0,0,1,-1,0]
def u(b,r,i=0):
 x=y=16
 for _ in q(1000):
  if x<0 or y<0 or x>32 or y>32:break
  i+=[2,-2][r[b[x,y]]=='L'];b[x,y]+=1;b[x,y]%=len(r);x+=h[i%8];y+=h[(i+1)%8]
 return b
for a in sys.argv[1:]:
 o=u(d(int),a)
 for j in q(33):p(''.join(str(o[i,j])for i in q(33)))
 p()
