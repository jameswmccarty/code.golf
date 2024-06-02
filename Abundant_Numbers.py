for i in range(201):
	if sum(x for x in range(1,i) if i%x==0)>i:
		print(i)
