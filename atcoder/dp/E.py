from sys  import stdin,stdout
from math import gcd
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    n,k=mp()
    knap=[li() for i in range(n)]
    s=sum([knap[i][1] for i in range(n)])
    dp=[[float('inf') for i in range(s+1)] for j in range(n+1)]
    dp[0][0]=0
    for i in range(1,n+1):
        a,b=knap[i-1]
        for j in range(s+1):
            if j==0:
                dp[i][j]=0
                
            elif j>=b:
                
                dp[i][j]=min(dp[i-1][j],dp[i-1][j-b]+a)
            else:
                dp[i][j]=dp[i-1][j]

    while dp[n][s]>k:
        s-=1
    pr(s)
        
                
        
for _ in range(1):
    solve()
