s=[0];c=0
while c<1000:
 print(s[-1]);c+=1
 if s.count(s[-1])<2:s+=[0]
 else:s+=[s[::-1][1:].index(s[-1])+1]
