def solve():
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    x=[]
    for i in range(k-n+1):
        x.append(l[i+n-1]-l[i])
    print(min(x))

solve()
