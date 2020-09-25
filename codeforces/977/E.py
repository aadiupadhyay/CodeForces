from sys  import stdin,stdout
from  collections import Counter
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF= float('inf')
def DFS(n):
    v[n]=True
    stack=[n]
    p=set()
    while stack:
        a=stack.pop()
        p.add(len(d[a]))
        for i in d[a]:
            if i==par[a]:
                continue
            else:
                if not v[i]:
                    v[i]=True
        
                    stack.append(i)
                    par[i]=a
    return p=={2}
    
n,m=mp()
d={i:[] for i in range(1,n+1)}
for i in range(m):
    a,b=mp()
    d[a].append(b)
    d[b].append(a)

v=[False for i in range(n+1)]
ans=0
par=[-1 for i in range(n+1)]
for i in range(1,n+1):
    if not v[i]:
        cycle=DFS(i)
        if cycle:
            ans+=1
pr(ans)
