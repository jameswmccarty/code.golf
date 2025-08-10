import sys
for b in sys.argv[1:]:
 d={}
 for c in b.split('\n'):
  x,y=c.split(' ')
  if x not in d:d[x]=set()
  if y in d:d[y].add(x)
  else:d[y]={x}
 o=''
 while d:
  for x,y in d.items():
   if not y:o+=x+' ';break
  for k in d:d[k].discard(x)
  del d[x]
 print(o)
