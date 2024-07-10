import sys;from fractions import Fraction as h
for a in sys.argv[1:]:o=f'{h(a)}';print(o if'/'in o else o+'/1')
