import sys
o=ord
for a in sys.argv[1:]:
 c,r,f=a[0],abs(o(a[3])-o(a[1])),abs(o(a[4])-o(a[2]))
 if c in'QK'and r<2and f<2or c in'BQ'and r==f or c=='N'and{r,f}=={1,2}or c in'RQ'and 0in{r,f}:print(a)
