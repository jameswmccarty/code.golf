v=[1,9,4879,5292,38962,5479453,16590564,19273023,13641364,8161912,19773073,24752475,627615]
for n in range(10,12000000):
 a=str(n*n);s=len(a)//2
 if(int(a[0:s])+int(a[s:]))==n:v+=[n]
for n in sorted(v):print(n)