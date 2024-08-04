import sys
z=print
for a in sys.argv[1:]:
	a=a.split('\n');s=[i[2]for i in a if len(i)>2]
	p=[i[2]for i in a if'>'in i][0]
	for c in a[-1][1:]:
		if c=='"':z(p,['Reject','Accept'][a[s.index(p)][1]=='F']);continue
		p=a[s.index(p)][a[0].index(c)]
