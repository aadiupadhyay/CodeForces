import math
a,b,n=map(int,input().split())
c=1
while True:
    if n==0:
        if c&1:
            print("1")
        else:
            print("0")
        break
    if c&1:
        n-=math.gcd(a,n)
    else:
        n-=math.gcd(b,n)
    c+=1
    
