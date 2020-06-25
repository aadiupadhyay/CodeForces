a,b=(map(int,input().split()))
z=min(a,b)
if z==a:
    b-=a
    y=b//2
else:
    a-=b
    y=a//2
print(z,y)
