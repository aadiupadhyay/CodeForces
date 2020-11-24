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
    d=Counter(l)
    x=[i for i in d if d[i]==1]
    if not x:
        print(-1)
        return 
    x.sort()
    print(l.index(x[0])+1)
        
            
    
for _ in range(inp()):
    solve()
