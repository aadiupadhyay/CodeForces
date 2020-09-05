
def solve():
    n,x,y=map(int,input().split())
    maxx=float('inf')
    for i in range(1,51):
        for j in range(1,51):
            l=[i+ k*j for k in range(n)]
            if (x in l) and (y in l) and l[-1]<maxx:
                maxx=l[-1]
                ans=l
    print(*ans)
        


for _ in range(int(input())):
    solve()
