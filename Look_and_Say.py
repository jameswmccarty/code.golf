def b(s):
	o,c,l='',0,s[0]
	for i in range(len(s)):
		if l==s[i]:
			c+=1
		else:
			o,c,l=o+str(c)+l,1,s[i]
	return o+str(c)+l
r='1'
for _ in range(20):
	print(r)
	r=b(r)
