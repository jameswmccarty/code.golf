import sys
for a in sys.argv[1:]:
 a=a.split();b=[0]*7;c=d=1;r=set();y=set()
 for i in map(int,a):[y,r][c].add((i,b[i]));b[i]+=1;c^=1
 for t,f in[(r,"Red"),(y,"Yellow")]:
  if any(all((x+_*q,y+_*w)in t for _ in(0,1,2,3))for q,w in((1,0),(0,1),(1,1),(1,-1))for x,y in t):print(f);d=0
 if d:print(["Draw",'-'][len(a)<42])
