r=range
def t(n):
 m,u,v,c,x,y=[[0]*n for i in r(n)],[0,1,0,-1],[1,0,-1,0],0,0,-1
 for i in r(n+n-1):
  for j in r((n+n-i)//2):x+=u[i%4];y+=v[i%4];m[x][y]=f'{c:>2}';c+=1
 return m
for i in t(10):print(*i)
