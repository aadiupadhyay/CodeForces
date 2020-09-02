n,m=map(int,input().split())
a=n>>1
c=0
b=n%2
for i in range(a+1):
    if (a+b)%m==0:
        print(a+b)
        c=1
        break
    a-=1
    b+=2
if c==0:
    print(-1)
