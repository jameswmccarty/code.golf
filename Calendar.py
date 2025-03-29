import sys,calendar as c
for a in sys.argv[1:]:print('\n'.join(c.TextCalendar().formatmonth(int(a[2:]),int(a[:2])).split('\n')[1:]))
