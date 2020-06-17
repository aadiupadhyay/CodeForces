def solve():
    a,k=map(int,input().split())
    c=0
    while a!=0:
        if a%k==0:
            a=a//k
            c+=1
        else:
            x=(a//k)*k
            c+=a-x
            a=x
    print(c)
for _ in range(int(input())):
    solve()
