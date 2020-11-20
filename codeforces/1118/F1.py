from sys  import stdin,stdout
from collections  import *
from math import gcd,floor,ceil
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

ans=0
n=inp()
l=[0]+li()
edge=[li() for i in range(n-1)]
d={i:[] for i in range(n+1)}
for i in edge:
    a,b=i
    d[a].append(b)
    d[b].append(a)
red,blue=0,0
for i in l:
    red+= (i==1)
    blue+= (i==2)
stack=[1]
v=[0 for i in range(n+1)]
RED=[1 if i==1 else 0 for i in l ]
BLUE=[1 if i==2 else 0 for i in l ]
par=[-1 for i in range(n+1)]
v[1]=1
while stack:
    a=stack[-1]
    f=0
    for i in d[a]:
        if not v[i]:
            v[i]=1
            stack.append(i)
            f=1
            par[i]=a
    if f==0:
        z=stack.pop()
        if stack:
            RED[par[z]]+=RED[z]
            BLUE[par[z]]+=BLUE[z]
for i in range(1,n+1):
    if par[i]!=-1:
        if RED[i]==red and BLUE[i]==0 or RED[i]==0 and BLUE[i]==blue:
            ans+=1
pr(ans)