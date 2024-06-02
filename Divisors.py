r=range
for i in r(1,101):
	print(*[n for n in r(1,i+1)if i%n==0])
