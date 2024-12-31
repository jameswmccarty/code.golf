import sys
for i in(0,1,2):print(''.join([' _     _  _     _  _  _  _  _ ','| |  | _| _||_||_ |_   ||_||_|','|_|  ||_  _|  | _||_|  ||_| _|'][i][int(b)*3:int(b)*3+3]for b in sys.argv[1]))
