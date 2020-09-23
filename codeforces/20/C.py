import sys
from sys  import stdin,stdout
from heapq import *

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

INF=float('inf')
n,m=mp()
d={i:[] for i in  range(1,n+1)}
for i in range(m):
    a,b,c=mp()
    d[a].append((b,c))
    d[b].append((a,c))

dis=[INF for i in range(n+1)]
dis[1]=0
h=[]
heappush(h,(0,1)) #distance,node
v=[False for i in range(n+1)]
par=[-1 for i in range(n+1)]
while h:
    cur_dis,cur_node=heappop(h)
    if v[cur_node]:
        continue
    v[cur_node]=True
    for node,distance in d[cur_node]:
        if cur_dis + distance < dis[node]:
            dis[node]=cur_dis + distance
            heappush(h,(dis[node],node))
            par[node]=cur_node

if not v[n]:
    pr(-1)
else:
        
    ans=[]
    ans.append(n)
    n=par[n]
    while par[n]>0:
        ans.append(n)
        n=par[n]
    ans.append(1)
    print(*reversed(ans))
