from sys  import stdin,stdout
from collections  import *
from math import ceil, floor , log
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")
 
mod=1000000007
INF=float('inf')
 
def solve():
    n,m= mp()
    d={i:[] for i in range(1,n+1)}
    deg={i:0 for i in range(1,n+1)}
    for i in range(m):
        a,b = mp()
        deg[a]+=1
        deg[b]+=1
        d[a].append(b)
        d[b].append(a)
    ma=-1
    val=0
    for i in deg:
        if deg[i]>ma:
            ma= deg[i]
            val= i
    v=[False for i in range(n+1)]
    q=deque()
    q.append(val)
    v[val]=True
    while q:
        a=q.popleft()
        for i in d[a]:
            if not v[i]:
                print(i,a)
                v[i]=True
                q.append(i)
    
 
 
 
for _ in range(1):
    #print('Case',str(_+1)+':')
    solve()
