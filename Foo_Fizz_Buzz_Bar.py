for i in range(1,1001):
	o=''
	if i%2==0:o+='Foo'
	if i%3==0:o+='Fizz'
	if i%5==0:o+='Buzz'
	if i%7==0:o+='Bar'
	print(o if o else i)
