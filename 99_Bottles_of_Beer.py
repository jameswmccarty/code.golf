q='bottle'
h=' of beer on the wall'
b=q+'s'+h
j=q+h
t='Take one down and pass it around,'
for i in range(99,2,-1):print(i,b+',',i,b[:15]+'.\n'+t,i-1,b+'.\n')
print('2 '+b+',','2 '+b[:15]+'.\n'+t,'1 '+j+'.\n\n1 '+j+', 1 '+j[:14]+'.\n'+t+' no more '+b+'.\n\nNo more '+b+', no more '+b[:15]+'.\nGo to the store and buy some more, 99 '+b+'.')
