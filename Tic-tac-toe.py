import sys
def t(a):return 3*a in b or any(all(b[i]==a for i in x)for x in[[0,5,10],[2,5,8],[0,4,8],[1,5,9],[2,6,10]])
for b in sys.argv[1:]:print([['-','X'][t('X')],'O'][t('O')])
