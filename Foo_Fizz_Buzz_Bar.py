i=1
while i<1001:o=''.join(v for k,v in((2,'Foo'),(3,'Fizz'),(5,'Buzz'),(7,'Bar'))if i%k==0);print(o if o else i);i+=1
