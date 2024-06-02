for i in range(1,101):
	t,f,z,b=i%3==0,i%5==0,'Fizz','Buzz'
	print(z+b if t&f else(z if t else(b if f else i)))
