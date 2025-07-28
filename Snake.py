import sys
z=print
m=[1,0,0,1,-1,0,0,-1]
for a in sys.argv[1:]:
 b={(0,0)};x=y=d=X=Y=0
 for c in a:
  if c=='F':x+=m[d];y+=m[d+1]
  elif c=='R':d+=2
  else:d-=2
  d%=8;b.add((x,y));X=max(x,X);Y=max(y,Y)
 for y in range(Y+1):
  for x in range(X+1):z(' #'[(x,y)in b],end='')
  z()
 z()
