from sys  import stdin,stdout

from collections import Counter

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

from bisect import bisect_left,bisect_right

mod=1000000007
INF=float('inf')
def DFS(n,d,v):
    v[n]=False
    stack=[n]
    while stack:
        a=stack.pop()
        for i in d[a]:
            if not v[i]:
                stack.append(i)
                v[i]=True
                
def solve():
    n,m=mp()
    d={i:[] for i in range(n+1)}
    for i in range(m):
        a,b=mp()
        d[a].append(b)
        d[b].append(a)
    ans=0
    v=[False for  i in range(n+1)]
    for i in range(1,n+1):
        if not v[i]:
            ans+=1
            DFS(i,d,v)
    pr(ans-1)
    
    
for _ in range(1):

    solve()
