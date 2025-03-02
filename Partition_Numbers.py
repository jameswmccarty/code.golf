t={0:1}
def k():
 e,o=1,3
 while 1:yield e;e+=1;yield o;o+=2
def q():
 n=1;yield n
 for x in k():n+=x;yield n
def p(n):
 if n in t:return t[n]
 if n<0:return 0
 o=i=0
 for v in q():
  y=p(n-v)
  if y==0:t[n]=o;return o
  o+=[1,1,-1,-1][i%4]*y;i+=1
for i in range(100):print(p(i))
