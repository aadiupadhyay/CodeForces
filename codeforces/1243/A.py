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

def solve():
    n=inp()
    l=li()
    l.sort()
    ans=0
    for i in range(n):
        ans=max(ans,min(l[i],n-i))
    pr(ans)
        
            
    
for _ in range(inp()):
    solve()
