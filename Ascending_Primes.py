b=lambda x: len(set(str(x)))==len(str(x))and list(str(x))==sorted(list(str(x)))
p=lambda x: not any(x%i==0 for i in range(2,x))
print('2')
for a in range(3,23456790,2):
	if b(a)and p(a):
		print(a)
