z=print
from fractions import Fraction as P
def f(n):
 a,b,c,d=0,1,1,n
 while 0<=c<=n:
  k=(n+b)//d
  a,b,c,d=c,d,k*c-a,k*d-b
  yield P(a,b)
z('0/1')
for a in[b for b in f(50)][:-1]:z(a)
z('1/1')
