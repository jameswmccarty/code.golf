import sys
from itertools import combinations as c
for a in sys.argv[1:]:
 for s in c(a.split(),3):
  if all(len({s[k][j]for k in(0,1,2)})in(1,3)for j in(0,1,2,3)):print(*s)
