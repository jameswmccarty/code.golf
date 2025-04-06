import sys
x='prnbqk'
z=print
for a in sys.argv[1:]:
 for c in a.split()[0]:
  b=c.lower()
  if b in x:z({1:'♟♜♞♝♛♚',0:'♙♖♘♗♕♔'}[c in x][x.index(b)],end='')
  if c.isdigit():z(int(c)*' ',end='')
  if c=='/':z()
 z('\n')
