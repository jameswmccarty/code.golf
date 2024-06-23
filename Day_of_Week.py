import sys
from datetime import date
for x in sys.argv[1:]:print(date(*map(int,x.split('-'))).strftime("%A"))
