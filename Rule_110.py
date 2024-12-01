r=range
o=[99]
for _ in r(100):
 print(''.join('█'if i in o else' 'for i in r(100)))
 o=[i for i in r(100)if 4*(i-1 in o)|2*(i in o)|(i+1 in o)not in[0,4,7]]
