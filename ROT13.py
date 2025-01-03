import sys
r=lambda a,b:chr(((ord(a)-b)+13)%26+b)
for a in sys.argv[1:]:print(''.join([x,r(x,[65,97][x>='a'])][x.isalpha()]for x in a))
