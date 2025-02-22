g=[0]
def a(n):b=g[-1]-n;return b if b>0and b not in g else g[-1]+n
for i in range(250):g+=[a(i)];print(g[-1])
