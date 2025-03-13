import sys
r=range
z=print
w=enumerate
def t(b,x,y,v):b[y*9+x]={v};e(b,x,y,v)
def e(b,x,y,v):
 for i in r(9):
  if i!=x:b[y*9+i].discard(v)
  if i!=y:b[i*9+x].discard(v)
 for i in r(3):
  for j in r(3):
   h=3*(x//3)+i;q=3*(y//3)+j
   if not(h==x and q==y):b[q*9+h].discard(v)
def d(b):
 z('┏━━━┯━━━┯━━━┳━━━┯━━━┯━━━┳━━━┯━━━┯━━━┓')
 for i in r(9):
  a,c,d,e,f,g,h,j,k=[str(tuple(x)[0])for x in b[i*9:i*9+9]]
  print(f'┃ {a} │ {c} │ {d} ┃ {e} │ {f} │ {g} ┃ {h} │ {j} │ {k} ┃')
  if i<8:z(['┠───┼───┼───╂───┼───┼───╂───┼───┼───┨','┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫'][i in(2,5)])
 z('┗━━━┷━━━┷━━━┻━━━┷━━━┷━━━┻━━━┷━━━┷━━━┛')
def y(b):
 while 1:
  if any(len(x)==0for x in b):return
  m=sum(len(x)for x in b)
  for i in r(81):
   if len(b[i])==1:
    e(b,i%9,i//9,tuple(b[i])[0])
  if any(len(x)==0for x in b):return
  if all(len(x)==1for x in b):d(b);exit()
  if sum(len(x) for x in b)==m:
   o=[i for i,x in w([len(y)for y in b])if x>1]
   for i in o:
    for v in tuple(b[i]):c=[set(x) for x in b];t(c,i%9,i//9,v);y(c);b[i].discard(v)
b=[{x for x in r(1,10)}for i in r(81)]
i=0
for a in sys.argv[1:]:
 for j,c in w(a):
  if c != '_':t(b,j,i,int(c))
 i+=1
y(b)
