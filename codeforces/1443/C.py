from sys  import stdin,stdout
from collections  import *
from math import gcd,floor,ceil
from bisect import bisect_left as bl
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

INF=float('inf')
mod=1000000007


def solve():
    n=inp()
    l=li()
    k=li()
    z=list(zip(l,k))
    z.sort()
    s=sum(k)
    x=0
    ans=INF

    for i in z:
        value=i[0]
        x+=i[1]
        left=s-x
        ans=min(ans,value + max(left-value,0))
        
    p=sum(l)
    h=list(zip(k,l))
    x=0
    val=0
    
    for i in h:
        x+=i[0]
        val+=i[1]
        left=p-val
        ans=min(ans,x+ max(left-x , 0))
        
    pr(ans)
    
    
    
for _ in range(inp()):
    solve()

   
