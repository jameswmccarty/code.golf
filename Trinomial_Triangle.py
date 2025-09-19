a=[1]
while len(a)<40:print(*a);a=[0,0]+a;a=[sum(a[j:j+3])for j in range(len(a))]
