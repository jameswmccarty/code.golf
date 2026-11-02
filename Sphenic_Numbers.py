p={x for x in range(2,3100)if not any(x%y==0for y in range(2,x))}
for a in sorted({i*j*k for i in p for j in p for k in p if i*j*k<1e4and len({i,j,k})==3}):print(a)
