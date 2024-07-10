import sys
l,g,q,j=set(),range,(-1,0,1),0
for r in sys.argv[1].split():
	i=0
	for c in r:
		if c=='#':l.add((i,j))
		i+=1
	j+=1
for j in g(32):
	o=''
	for i in g(32):
		v=sum((i+a,j+b)in l and a|b!=0for a in q for b in q)
		if((i,j)in l and v in(2,3))|((i,j)not in l and v==3):o+='#'
		else:o+='.'
	print(o)
