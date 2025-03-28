import sys
r=range
s=lambda x,a,y,b:len({*r(x,x+a)}.intersection({*r(y,y+b)}))
for q in sys.argv[1:]:x,y,w,h,q,e,t,u=map(int,q.split());print(s(x,w,q,t)*s(y,h,e,u))
