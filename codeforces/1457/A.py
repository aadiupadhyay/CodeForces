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
    n,m,r,c= mp()
    x=abs(r-n)+abs(c-m)
    y=abs(r-1)+abs(c-1)
    a=abs(r-n)+abs(c-1)
    b=abs(r-1)+abs(c-m)
    pr(max(x,max(y,max(a,b))))
        
            
    
for _ in range(inp()):
    solve()
