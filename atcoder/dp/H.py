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
    n,m = mp()
    l=[st() for i in range(n)]
    dp=[[0 for i in range(m)] for j in range(n)]
    i=0
    while i<m:
        if l[0][i]=='#':
            break
        dp[0][i]=1
        i+=1
    i=0
    while i<n:
        if l[i][0]=='#':
            break
        dp[i][0]=1
        i+=1
    for  i in range(1,n):
        for j in range(1,m):
            if l[i][j]=='.':
                dp[i][j] = (dp[i-1][j]%mod + dp[i][j-1]%mod )%mod
        
    print(dp[-1][-1])     
    
solve()
