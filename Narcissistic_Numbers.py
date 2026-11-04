for i in range(1,1001):
 for b in range(2,i+1):
  p=[];q=i
  while q:p+=[q%b];q=q//b
  if sum(x**len(p)for x in p)==i:print(i);break
