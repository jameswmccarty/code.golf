import sys
def e(x,c,o,l):
 for u in x:
  if u==l:c+=1
  else:
   if l!=' ':o+=chr(ord("  ADGJMPTW"[int(l)])+c)
   c=0;l=u
 return o
for a in sys.argv[1:]:print(e(a+' ',0,'',' '))
