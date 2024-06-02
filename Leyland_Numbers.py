r,p=range,pow
for v in sorted({p(x,y)+p(y,x)for x in r(1,37)for y in r(2,x+1)})[:107]:
	print(v)
