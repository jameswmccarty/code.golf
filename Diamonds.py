r=range
def d(s):l=''.join(str(s+1)for s in r(s));print(' '*(10-s)+l+l[::-1][1:])
for i in r(1,10):
 for a in[x for x in r(1,i+1)]+[x for x in r(i-1,-1,-1)]:d(a)
