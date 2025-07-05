def g(y,h,x=-2,l=''):
 while x<=0.5:
  p=x+1j*y;z=0;c='█'
  for i in range(1064):
   if abs(z)>=h:c='▒';break
   z=z**2+p
  l+=c;x+=2.5/80
 return l
y,s=-1,[]
while y<0:s+=[g(y,2)];y+=.05
b=s[::-1]
s+=[g(0,2.1)]
s+=b
for l in s:print(l)
