from sys  import stdin,stdout
from collections  import *
from math import ceil, floor , log, gcd
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
    x=sorted(l)
    s=sum(l)
    a=sum(x[:n])
    b=s-a
    if b==a:
        pr(-1)
        return
    print(*x)
    
    

for _ in range(1):
    solve()
