import sys
r,k=[0,1,2,3,4,5,6,7,8,9],[-1,0,1]
for b in sys.argv[1:]:
 b=b.split()
 for y in r:print(''.join(str([sum(b[y+i][x+j]=='X'if(x+j in r)&(y+i in r)&(i|j)else 0for i in k for j in k),'F'][b[y][x]=='X'])for x in r))
 print()
