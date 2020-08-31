
n,m=map(int,input().split())
ans=0
l=list(map(int,input().split()))

d=[0 for i in range(m)]
for i in l:
    d[i-1]+=1

val=[i for i in d]

for i in range(len(val)-2,-1,-1):
    val[i]+=val[i+1]

for i in range(m-1):
    ans+=d[i]*(val[i+1])

print(ans)
