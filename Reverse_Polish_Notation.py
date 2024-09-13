import sys
def s(a,t=[]):
	for e in a:
		if e in'+-*/':l=t.pop();r=t.pop();t+=[eval(str(r)+e+str(l))]
		else:t+=[e]
	print(int(t[-1]))
for a in sys.argv[1:]:s(a.split())
