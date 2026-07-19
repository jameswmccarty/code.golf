u,r=[1,2],range
for t in r(248):
 d,m=dict(),len(u)
 for i in r(m):
  for j in r(i+1,m):
   p=u[i]+u[j]
   if p in d:d[p]+=1
   else:d[p]=1
 u+=[min(k for k in d.keys()if d[k]==1 and k>max(u))]
for e in u:print(e)
