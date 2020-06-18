def solve():
    c=0
    a,b,n=map(int,input().split())
    while a<=n and b<=n:
        x=max(a,b)
        if x==a:
            b+=a
            c+=1
        else:
            a+=b
            c+=1
    print(c)


for _ in range(int(input())):

    solve()
