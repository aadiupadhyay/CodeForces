import bisect
x,n=map(int,input().split())
l=list(map(int,input().split()))
k=[0]*(102)
for i in l:
    k[i]=1
s=10000
for i in range(102):
    if k[i]==1:
        continue
    if abs(x-i)<s:
        s=abs(x-i)
        ans=i
print(ans)
    
