g=[0]
def a(n):b=g[0]-n;return[g[0]+n,b][b>0and~(b in g)]
for i in range(250):g=[a(i)]+g;print(g[0])
