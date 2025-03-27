import sys,itertools as c
for a in sys.argv[1:]:
 for s,d,f in c.combinations(a.split(),3):
  if all(len({s[j],d[j],f[j]})in(1,3)for j in(0,1,2,3)):print(s,d,f)
