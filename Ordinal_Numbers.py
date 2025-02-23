import sys
for a in sys.argv[1:]:print(a+'th'if len(a)>1and a[-2]=='1'else a+[0,'st','nd','rd'][int(a[-1])]if a[-1]in'123'else a+'th')
