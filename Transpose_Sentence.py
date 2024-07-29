import sys
for a in sys.argv[1:]:
	a=[list(x)for x in a.split()]
	while any(a):print(''.join(x.pop(0)if x else''for x in a),end=' ')
	print()
