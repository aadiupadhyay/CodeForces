from sys  import stdin,stdout
from math import gcd
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    n=inp()
    knap=[li() for i in range(n)]
    if n==1:
        print(max(knap[0]))
        return
    dp=[[0 for i in range(3)] for j in range(n)]
    dp[0]=knap[0]
    for i in range(1,n):
        dp[i][0]=max(dp[i-1][1]+knap[i][0],dp[i-1][2]+knap[i][0])
        dp[i][1]=max(dp[i-1][0]+knap[i][1],dp[i-1][2]+knap[i][1])
        dp[i][2]=max(dp[i-1][0]+knap[i][2],dp[i-1][1]+knap[i][2])
    pr(max(dp[-1]))

                
        
for _ in range(1):
    solve()
