import sys
for e in sys.argv[1:]:
	s=[]
	m=list(map(ord,e))
	d=[0]*len(m)
	i=p=0
	while(i>=0and i<len(m)):
		v=m[i]
		if v==91:
			if d[p]!=0:s+=[i-1]
			else:
				c=1
				while c:
					i+=1
					if m[i]==91:c+=1
					elif m[i]==93:c-=1
		elif v==93:i=s.pop()
		elif v==62:p+=1
		elif v==60:p-=1
		elif v==43:d[p]+=1
		elif v==45:d[p]-=1
		elif v==46:print(chr(d[p]),end='')
		i+=1
