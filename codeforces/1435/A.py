from sys  import stdin,stdout
from collections  import *
from math import ceil, floor
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
    x=[l[i] for i in range(n//2-1,-1,-1)]
    y=[l[i] for i in range(n-1,n//2 -1,-1)]
    ans=[-1*i for i in y]+x
    print(*ans)
    
            
    
    
for _ in range(inp()):
    solve()

