import math
n,k=map(int,input().split())
if k<=n//2:
    print(2*k-1)
else:
    i=k-math.ceil(n/2)
    if i!=0:
        print(2*i)
    else:
        print(n)
