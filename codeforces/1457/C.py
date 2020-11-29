from sys  import stdin,stdout
from collections  import *
from math import gcd,floor,ceil
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():
    n,p,k=mp()
    s=st()
    x,y = mp()
    ans=INF
    dp=[0 for i in range(n)]
    for i in range(n-1,-1,-1):
        if s[i]=='0':
            dp[i]+=x
        if i+k<n:
            dp[i]+=dp[i+k]
    for i in range(p-1,n):
        ans= min(ans,dp[i] + (i-p+1)*y)
        
            
    pr(ans)
for _ in range(inp()):
    solve()
