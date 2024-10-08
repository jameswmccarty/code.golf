def p():
	q,r,t,k,n,l=1,0,1,1,3,3
	while 1:
		if 4*q+r-t<n*t:yield str(n);w=10*(r-n*t);n=((10*(3*q+r))//t)-10*n;q*=10;r=w
		else:w=(2*q+r)*l;b=(q*(7*k)+2+(r*l))//(t*l);q*=k;t*=l;l+=2;k+=1;n=b;r=w
a=''
for d in p():
	a+=d
	if len(a)==1001:break
print('3.'+a[1:])
