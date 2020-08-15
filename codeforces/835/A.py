s,v1,v2,t1,t2=map(int,input().split())
z1=s*v1+2*t1
z2=s*v2+2*t2
if z1>z2:
    print("Second")
elif z2>z1:
    print("First")
else:
    print("Friendship")