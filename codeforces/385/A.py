n,b=map(int,input().split())

l=list(map(int,input().split()))
ans=0
for i in range(n-1):
    ans=max(ans,l[i]-l[i+1]-b)
print(ans)
