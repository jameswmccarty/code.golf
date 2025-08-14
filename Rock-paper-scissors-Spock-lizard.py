import sys
m="✂ cuts 📄 covers 💎 crushes 🦎 poisons 🖖 smashes ✂ decapitates 🦎 eats 📄 disproves 🖖 vaporizes 💎 crushes ✂ . .".split(' ')
for a in sys.argv[1:]:
 if a[0]==a[1]:print("Tie")
 else:
  for i,e in enumerate(m):
   if e==a[0]and m[i+2]==a[1]or e==a[1]and m[i+2]==a[0]:print(' '.join(m[i:i+3]))
