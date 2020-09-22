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
    dp=[0 for i in range(k+1)]
    for i in range(n):
        for j in range(k,knap[i][0]-1,-1):
            dp[j]=max(dp[j],dp[j-knap[i][0]]+knap[i][1])
    pr(dp[-1])
                
        
for _ in range(1):
    solve()
