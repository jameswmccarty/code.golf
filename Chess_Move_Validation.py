import sys
o=ord
for a in sys.argv[1:]:
 c,r,f=a[0],abs(o(a[3])-o(a[1])),abs(o(a[4])-o(a[2]))
 if c=='K'and {r,f}.issubset({0,1})or c=='B'and r==f or c=='N'and{r,f}=={1,2}or c=='R'and 0in{r,f}or c=='Q'and(r+f==1 or r==f or 0in{r,f}):print(a)
