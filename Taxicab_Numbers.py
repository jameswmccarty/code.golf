n=set()
t=set()
for x in range(1,500):
 for y in range(x,500):
  i=x**3+y**3
  if i in n and i<1e8:t.add(i)
  n.add(i)
for z in sorted(t):print(z)
