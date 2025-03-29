import sys
for a in map(int,sys.argv[1:]):print(bin(a^a>>1)[2:])
