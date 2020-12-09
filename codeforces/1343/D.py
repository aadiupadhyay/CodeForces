t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    dp=[0]*(2*k+2)
    i=0
    j=n-1
    while i<j:
        x,y=min(a[i],a[j]),max(a[i],a[j])
        dp[0]+=2
        dp[x+1]-=1
        dp[x+y]-=1
        dp[x+y+1]+=1
        dp[y+k+1]+=1
        i+=1
        j-=1
    
    for i in range(1,len(dp)):
        dp[i]+=dp[i-1]
    print(min(dp))