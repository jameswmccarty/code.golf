import sys
def e(x,c,o,l):
 for u in x+l:
  if u!=l:
   if l!=' ':o+=chr(ord("  ADGJMPTW"[int(l)])+c)
   c=-1;l=u
  c+=1
 return o
for a in sys.argv[1:]:print(e(a,0,'',' '))
