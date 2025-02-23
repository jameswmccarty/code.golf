s=[];c=0
while c<1000:
 x=0
 while c<1000:
  s=[s.count(x)]+s;x+=1;print(s[0]);c+=1
  if s[0]==0:break
