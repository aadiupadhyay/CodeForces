from sys  import stdin,stdout
from collections  import *
from math import *
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')
ANS=[]
def solve():
    n=inp()
    l=li()
    i=0
    j=1
    d={i:[] for i in range(n)}
    while i<n:
        if j==n:
            break
        d[i].append(j)
        a=l[j]
        j+=1
        while j<n and l[j]>=a:
            d[i].append(j)
            a=l[j]
            j+=1
        i+=1
    level={}
    level[0]=0
    q=deque()
    q.append((0,0))
    ans=0
    visited=[False for i in range(n)]
    while q:
        a,b=q.popleft()
        for i in d[a]:
            if not visited[i]:
                visited[i]=True
                level[i]=b+1
                q.append((i,level[i]))
                ans=max(ans,level[i])
    pr(ans)
                
                
        
            
    
for _ in range(inp()):
    solve()
#pr('\n'.join(map(str,ANS)))
