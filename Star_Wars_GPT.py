import sys
c=dict();a=sys.argv[1].split('\n')
w=a[0].split()
for i,g in enumerate(w):
 if i<len(w)-1:
  if g not in c:c[g]=dict();c[g][0]=0
  if w[i+1]not in c[g]:c[g][w[i+1]]=0
  c[g][w[i+1]]+=1;c[g][0]=max(c[g][0],c[g][w[i+1]])
for b in a[1:]:
 for k,v in c[b].items():
  if k!=0and v==c[b][0]:print(k);break
