z,b='Fizz','Buzz'
for i in range(1,101):
	t,f=i%3==0,i%5==0
	m=i
	if f:
		m=b
	if t:
		m=z
	if t&f:
		m=z+b
	print(m)
