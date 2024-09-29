import sys
m={0:0,1:2,2:4,3:6,4:8,5:1,6:3,7:5,8:7,9:9}
def v(a,t=0):
    for e in a.split():t+=m[int(e[0])]+int(e[1])+m[int(e[2])]+int(e[3])
    return t%10==0
for a in sys.argv[1:]:
    if(v(a)):print(a)
