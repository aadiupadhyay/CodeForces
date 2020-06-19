def solve():
    c=0
    n,k=map(int,input().split())
    a=(k-1)*1
    x=n-k+1
    b=(k-1)*2
    y=n-(2*k)+2
    if x>0 and x&1:
        c=1
        print("YES")
        print("1 "*(k-1)+str(x))

    elif y>0 and not y&1:
        c=1
        print("YES")
        print("2 "*(k-1)+str(y))
    if c==0:
        print("NO")
        



for _ in range(int(input())):

    solve()
