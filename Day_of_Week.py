import sys,datetime
for x in sys.argv[1:]:print(datetime.date(*map(int,x.split('-'))).strftime("%A"))
