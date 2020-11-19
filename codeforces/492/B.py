n,k=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
ans=max(l[0]-0,k-l[-1])
for i in range (1,n):
  ans=max(ans,(l[i]-l[i-1])/2)
print(ans)