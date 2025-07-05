def g(y,h,x=-2,l=''):
 while x<=0.5:
  p=x+1j*y;z=0;c=1
  for i in range(1064):
   if abs(z)>=h:c=z=0
   z=z**2+p
  l+='▒█'[c];x+=2.5/80
 return [l]
y,s=-1,[]
while y<0:s+=g(y,2);y+=.05
for l in s+g(0,2.1)+s[::-1]:print(l)
