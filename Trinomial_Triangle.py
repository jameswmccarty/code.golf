a,c,z=[1]*3,[0,0],print
z(1)
for i in range(19):z(*a);a=c+a+c;a=[sum(a[j:j+3])for j in range(len(a)-2)]
