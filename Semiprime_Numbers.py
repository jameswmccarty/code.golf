p={x for x in range(2,5000)if not any(x%y==0for y in range(2,x))}
for a in sorted({i*j for i in p for j in p if i*j<10000}):print(a)
