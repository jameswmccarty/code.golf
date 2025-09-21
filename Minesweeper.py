import sys
r=[0,1,2,3,4,5,6,7,8,9]
def c(x,y,b,t=0):
 for j in(-1,0,1):
  for i in (-1,0,1):
   if i|j:
    if(x+j in r)&(y+i in r):t+=b[y+i][x+j]=='M'
 return[t,'X'][b[y][x]=='M']
for b in sys.argv[1:]:
 for y in r:print(''.join(str(c(x,y,b.split()))for x in r))
 print()
