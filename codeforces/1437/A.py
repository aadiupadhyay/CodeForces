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
    a,b = mp()
    if a<<1 <= b:
        pr('NO')
    else:
        pr('YES')
    
for _ in range(inp()):
    solve()
