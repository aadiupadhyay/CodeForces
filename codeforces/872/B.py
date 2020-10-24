from sys  import stdin,stdout
from collections  import *

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():
    n,m= mp()
    l=li()
    a=max(l)
    x=[]
    p=sorted(l)
    if m==1:
        pr(min(l))
        return
    if m>=3:
        pr(a)
        return
    preMI=[l[0]]
    sufMI=[l[-1]]
    for i in range(1,n):
        preMI.append(min(preMI[-1],l[i]))
        sufMI.append(min(sufMI[-1],l[n-i-1]))
    ans= -INF

    for i in range(n):
        ans= max(ans,preMI[i],sufMI[i])
    pr(ans)
    
for _ in range(1):
    solve()
