from math import ceil
n=int(input())
l=list(map(int,input().split()))
d={3:0,1:0,2:0,4:0}
for i in l:
    d[i]+=1

ans=d[4]
c=min(d[1],d[3])
ans+=c
if c==d[1]:
    ans+=(d[3]-c)
    ans+=(d[2]//2)+(d[2]%2)
else:
    d[1]-=c
    ans+=(d[2]//2)
    d[2]=d[2]%2
    pair=(d[1]//2) + (d[1]%2)
    if d[2]:
        ans+=1
        d[1]-=2
        ans+=ceil(d[1]/4)
    else:
        ans+=ceil(d[1]/4)
print(ans)
