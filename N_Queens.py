from itertools import permutations as p
r=range
def c(s):
	i=0;m=len(s)
	while i<m:
		j=n=int(s[i]);k=i
		while k<m-1:
			k+=1;j+=1;n-=1;v=int(s[k])
			if v==j or v==n:return 0
		j=n=int(s[i]);k=i
		while k>1:
			k-=1;j+=1;n-=1;v=int(s[k])
			if v==j or v==n:return 0
		i+=1
	return 1
for z in r(4,9):
	for s in p([x+1 for x in r(z)]):
		if c(s):print(''.join(str(x) for x in s))
