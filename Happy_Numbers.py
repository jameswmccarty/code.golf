h=lambda x:sum(pow(int(y),2)for y in str(x))
for i in range(200):
	a,n=[],h(i)
	while n not in a:a+=[n];n=h(n)
	if 1 in a:print(i)
