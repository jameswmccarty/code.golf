n=[i for i in range(8811) if i&1]
i,z=1,print
z('1')
while i<1000:
	c=n[i]
	z(c)
	del n[c-1::c]
	i+=1
