n=int(input())
l=list(map(int,input().split()))
z=max(l)
x=min(l)
c=l[::-1]
a=l.index(z)
b=c.index(x)
if (n-1)-b<=a:
    print(a+b-1)
else:
    print(a+b)
