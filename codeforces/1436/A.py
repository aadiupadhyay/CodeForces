from sys  import stdin,stdout
from collections  import *
from math import *
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():
    n,m=mp()
    l=li()
    s=sum(l)
    pr('YES' if s==m else 'NO')
        
    
    
for _ in range(inp()):
    solve()
