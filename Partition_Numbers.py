t={0:1}
def q():
 n=e=1;o=3
 while 1:yield n;n+=e;e+=1;yield n;n+=o;o+=2
def p(n):
 if n in t:return t[n]
 if n<0:return 0
 o=i=0
 for v in q():
  y=p(n-v)
  if y==0:t[n]=o;return o
  o+=[1,1,-1,-1][i%4]*y;i+=1
for i in range(100):print(p(i))
