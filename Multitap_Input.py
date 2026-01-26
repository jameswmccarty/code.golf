import sys
def e(x,c,o,l):
 for u in x:
  if u==l:c+=1
  else:
   if l!=' ':o+=chr([32,0,65,68,71,74,77,80,84,87][ord(l)-48]+c)
   c=0;l=u
 return o
for a in sys.argv[1:]:print(e(a+' ',0,'',' '))
