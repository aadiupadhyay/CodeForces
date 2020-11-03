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
    l=[inp() for i in range(3)]
    a=l[0]
    for i in range(a,0,-1):
        if l[1]>=2*i and l[2]>=4*i:
            pr(7*i)
            return
    pr(0)
        
            
    
    

for _ in range(1):
    solve()
