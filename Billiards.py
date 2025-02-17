import sys
d={(1,1):'\\',(1,-1):'/',(-1,1):'/',(-1,-1):'\\'};z=print
for a in sys.argv[1:]:
 m,n=map(int,a.split());b={};x=y=u=v=1
 while(x,y)not in b:
  b[(x,y)]=d[(u,v)];p,q=u,v
  if x+u>m or x+u<1:p*=-1;x-=u
  if y+v>n or y+v<1:q*=-1;y-=v
  x+=u;y+=v;u,v=p,q
 for i in range(1,m+1):
  for j in range(1,n+1):
   z(b[(i,j)]if(i,j)in b else' ',end='')
  z()
 z()
