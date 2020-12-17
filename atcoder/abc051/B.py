k,s = map(int,input().split())
ans=0
for i in range(k+1):
  for j in range(k+1):
    x=s-i-j
    if x>=0 and x<=k:
      ans+=1
print(ans)