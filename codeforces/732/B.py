# aadiupadhyay mobile se code krte hue 
n,k = map(int,input().split())
l = list(map(int, input ().split()))
ans= 0 
for i in range(1,n):
  if l[i]+l[i-1] < k:
    c= k-l[i]-l[i-1]
    ans+=c
    l[i]+=c
print(ans)
print(*l)