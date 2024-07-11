for i in range(200):
	a,n=[],i
	while n not in a:a+=[n];n=sum(int(y)**2for y in str(n))
	if 1 in a:print(i)
