import sys
r,k=[0,1,2,3,4,5,6,7,8,9],[-1,0,1]
def c(x,y,b,t=0):
 for j in k:
  for i in k:
   if i|j:
    if(x+j in r)&(y+i in r):t+=b[y+i][x+j]=='M'
 return[t,'X'][b[y][x]=='M']
for b in sys.argv[1:]:
 for y in r:print(''.join(str(c(x,y,b.split()))for x in r))
 print()
