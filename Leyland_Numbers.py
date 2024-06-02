for v in sorted({pow(x,y)+pow(y,x) for x in range(1,37)for y in range(2,x+1)})[:107]:
	print(v)
