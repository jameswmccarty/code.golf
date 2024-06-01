n=[i for i in range(8811) if i&1]
i=1
print('1')
while i<1000:
	c=n[i]
	print(c)
	del n[c-1::c]
	i+=1
