import sys
r=range
s=lambda x,a,y,b:len({*r(x,a)}.intersection({*r(y,b)}))
for q in sys.argv[1:]:x,y,w,h,q,e,t,u=map(int,q.split());print(s(x,x+w,q,q+t)*s(y,y+h,e,e+u))
