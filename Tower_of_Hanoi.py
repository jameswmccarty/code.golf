def s(z,c,d):
 if z!=0:s(z-1,c,c^d);print(c,'->',d);s(z-1,c^d,d)
s(9,1,3)
