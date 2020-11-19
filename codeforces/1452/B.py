from sys  import stdin,stdout
from collections  import *
from math import gcd,floor,ceil
from bisect import bisect_left
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
    s=sum(l)
    x=n-1
    y= ceil(s/x)
    z= x*y
    if l[-1]>y:
        z=l[-1]*x
    pr(z-s)

            
    
            
for _ in range(inp()):
    solve()
