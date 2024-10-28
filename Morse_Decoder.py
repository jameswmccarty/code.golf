import sys
a=' ETIANMSURWDKGOHVF L PJBXCYZQ  54 3   2       16       7   8 90'
def i(s,x=0):
 for c in s.split():x=2*x+{'▄':1,'▄▄▄':2}[c]
 return x
for d in sys.argv[1].split(' '*10):print(''.join(a[i(e)]for e in d.split('   ')),end=' ')
