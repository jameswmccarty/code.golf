r=range
s=lambda x:sum(int(n)for n in str(x))
def f(n):
 p='';o=n
 while n!=1:
  for j in r(2,n+1):
   if n%j==0:
    if j!=o:p+=str(j)
    n//=j;break
 return p
for k in r(1,9986):
 if s(k)==s(f(k)):print(k)
