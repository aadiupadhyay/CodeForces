n,m=map(int,input().split())
l=list(map(int,input().split()))

if sum(l) + 10*(n-1) >m:
    print(-1)
else:
    ans=2*(n-1)
    m-=(sum(l) + 10*(n-1))
    ans+=m//5
    print(ans)
