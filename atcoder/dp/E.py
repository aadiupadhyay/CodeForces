INF=10**18
n,m=map(int,input().split())
w=[0]*n
v=[0]*n
for i in range(n):
  w[i],v[i]=map(int,input().split())
k=sum(v)
dp=[INF]*(k+1)
dp[0]=0
for i in range(n):
  for j in range(k,-1,-1):
    if j>=v[i] and dp[j-v[i]]!=INF:dp[j]=min(dp[j],dp[j-v[i]]+w[i])
for i,x in enumerate(dp):
  if x<=m:ans=i
print(ans)