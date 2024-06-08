f=lambda x:x if x<=1else f(x-1)+f(x-2)
for i in range(31):print(f(i))
