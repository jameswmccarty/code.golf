import sys
z=print
for a in sys.argv[1:]:
	a=int(a);p='a';b=abs(a);m=b//60;h=m//60;d=h//24;w=d//7;o=d//30;y=d//365;g='ago'
	if 0==a:z('now');continue
	v,q=min(x for x in[(b,'second'),(m,'minute'),(h,'hour'),(d,'day'),(w,'week'),(o,'month'),(y,'year')]if x[0]>0)
	if 'ho'in q:p+='n'
	if v==1:
		if a<0:z(p,q,g)
		else:z('in',p,q)
	else:
		if a<0:z(v,q+'s',g)
		else:z('in',v,q+'s')
