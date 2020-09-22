import sys
from sys  import stdin,stdout
from math import gcd
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

sys.setrecursionlimit(10**6)
mod=1000000007
def DFS(p):
    if v[p]:
        return L[p]
    v[p]=True
    for i in d[p]:
        if not v[i]:
            DFS(i)
        L[p]=max(L[p],1+L[i])

            
    

n,m=mp()
d={i:[] for i in range(1,n+1)}
for _ in range(m):
    a,b=mp()
    d[a].append(b)
v=[False for  i  in range(n+1)]
L=[0 for i in range(n+1)]

for i in range(1,n+1):
    if not v[i]:
        DFS(i)

    
pr(max(L))
