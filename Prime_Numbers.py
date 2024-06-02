p=lambda x: not any(x%i==0 for i in range(2,x))
for a in range(2,101):
	if p(a):
		print(a)
