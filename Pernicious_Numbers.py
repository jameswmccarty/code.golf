r,p=range,lambda x:x>1and not any(x%i==0for i in r(2,x))
for i in r(10001):
 if p(bin(i).count('1')):print(i)
