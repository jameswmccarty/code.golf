import sys
x='PRNBQK'
z=print
for a in sys.argv[1:]:
 for c in a.split()[0]:
  b=c.upper()
  if b in x:z(['♟♜♞♝♛♚','♙♖♘♗♕♔'][c in x][x.index(b)],end='')
  elif c=='/':z()
  else:z(int(c)*' ',end='')
 z('\n')
