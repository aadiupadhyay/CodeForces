from sys  import stdin,stdout
from collections import deque
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    n,m=mp()
    l=li()
    l=[-1]+l
    d={i:[] for i in range(n+1)}
    v=[False for  i in range(n+1)]
    for i in range(n-1):
        a,b=mp()
        d[a].append(b)
        d[b].append(a)
    now=l[1]
    ans=0
    q=deque()
    q.append((1,now))
    v[1]=True
    while q:
        a,b=q.popleft()

        f=0
        v[a]=True
        for  i in d[a]:
            c=b
            if not v[i]:
                f=1
                v[i]=True
                if l[i]==0:
                    c=0
                else:
                    
                    c+=1
                if c<=m:
                    q.append((i,c))
        if f==0:
            ans+=1
       
    pr(ans)
                    
for _ in range(1):
    solve()
