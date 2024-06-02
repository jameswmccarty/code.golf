z,b='Fizz','Buzz'
for i in range(1,101):
	t,f=i%3==0,i%5==0
	if t&f:
		m=z+b
	elif f:
		m=b
	elif t:
		m=z
	else:
		m=i
	print(m)
