r=range
for i in r(201):
	if sum(x for x in r(1,i)if i%x==0)>i:
		print(i)
