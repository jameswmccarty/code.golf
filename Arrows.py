import sys
x=y=0
for c in sys.argv[1:]:
	for k,(a,b) in {'↙↲⇙':(-1,-1),'←⇐⇦':(-1,0),'↖↰⇖':(-1,1),'↓⇓⇩':(0,-1),'↑⇑⇧':(0,1),'↘↳⇘':(1,-1),'→⇒⇨':(1,0),'↗↱⇗':(1,1)}.items():
		if c in k:
			x,y=x+a,y+b
	print(x,y)
