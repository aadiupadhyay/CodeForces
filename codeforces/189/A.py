
def rib(n,a,b,c):
    if n==0:
        dp[n]=0
        return 0
    if n>=a:
        if dp[n-a]:
            ans1=dp[n-a]
        else:
            ans1=rib(n-a,a,b,c)
            dp[n-a]=ans1

    else:
        ans1=-10000

    if n>=b:
        if dp[n-b]:
            ans2=dp[n-b]
        else:
            ans2=rib(n-b,a,b,c)
            dp[n-b]=ans2
    else:
        ans2=-10000

    if n>=c:
        if dp[n-c]:
            ans3=dp[n-c]
        else:
            ans3=rib(n-c,a,b,c)
            dp[n-c]=ans3
    else:
        ans3=-100000

    dp[n]=1+max(ans1,ans2,ans3)

    return dp[n]

import sys
sys.setrecursionlimit(10000)
n,a,b,c=map(int,input().split())
dp=[0]*(n+1)
print(rib(n,a,b,c))
##print(dp)
