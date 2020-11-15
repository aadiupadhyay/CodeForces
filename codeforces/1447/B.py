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
    n,m= mp()
    l=[li() for  i in range(n)]
    ma= INF
    s=0
    c=0
    for i in l:
        for j in i:
            s+=abs(j)
            if j<0:
                c+=1
            ma = min(ma,abs(j))
    if c%2==0:
        
        pr(s)
    else:
        pr(s-2*ma)


    
        
    

for _ in range(inp()):
    solve()
