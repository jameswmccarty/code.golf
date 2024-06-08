import sys
a=sys.argv
def f(c,p):
    if p==0:return 0
    if not c:return 2**64
    return min(p//c[0]+f(c[1:],p%c[0]),f(c[1:],p))
print(f([int(x)for x in a[1].split(',')],int(a[2])))
